#include <bits/stdc++.h>
using namespace std;

static const int MOD = 663224321;
static const int PRIMITIVE_ROOT = 3;  // primitive root for MOD = 3·2^23 + 1
using ll = long long;

// Fast exponentiation modulo MOD
ll modpow(ll a, ll e, ll m = MOD) {
    ll r = 1;
    while (e) {
        if (e & 1) r = r * a % m;
        a = a * a % m;
        e >>= 1;
    }
    return r;
}

// Number Theoretic Transform (in-place)
// if invert = false, does forward NTT; otherwise inverse NTT
void ntt(vector<int> &a, bool invert) {
    int n = a.size();
    // bit-reversal permutation
    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1) j ^= bit;
        j ^= bit;
        if (i < j) swap(a[i], a[j]);
    }
    // NTT layers
    for (int len = 2; len <= n; len <<= 1) {
        ll wlen = modpow(PRIMITIVE_ROOT, (MOD - 1) / len);
        if (invert) wlen = modpow(wlen, MOD - 2);
        for (int i = 0; i < n; i += len) {
            ll w = 1;
            for (int j = 0; j < len/2; j++) {
                int u = a[i + j];
                int v = (int)(a[i + j + len/2] * w % MOD);
                a[i + j] = u + v < MOD ? u + v : u + v - MOD;
                a[i + j + len/2] = u - v >= 0 ? u - v : u - v + MOD;
                w = w * wlen % MOD;
            }
        }
    }
    if (invert) {
        ll inv_n = modpow(n, MOD - 2);
        for (int &x : a) x = x * inv_n % MOD;
    }
}

// Multiply two polynomials via NTT
vector<int> multiply(const vector<int> &a, const vector<int> &b) {
    int sz = 1;
    while (sz < (int)(a.size() + b.size() - 1)) sz <<= 1;
    vector<int> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    fa.resize(sz);
    fb.resize(sz);
    ntt(fa, false);
    ntt(fb, false);
    for (int i = 0; i < sz; i++) {
        fa[i] = (ll)fa[i] * fb[i] % MOD;
    }
    ntt(fa, true);
    fa.resize(a.size() + b.size() - 1);
    return fa;
}

// Compute the multiplicative inverse of series A modulo x^n,
// i.e. find R such that A(x)*R(x) ≡ 1 (mod x^n)
vector<int> invert_series(const vector<int> &A, int n) {
    vector<int> R(1);
    R[0] = modpow(A[0], MOD - 2);  // inverse of constant term
    while ((int)R.size() < n) {
        int m = R.size() << 1;
        if (m > n) m = n;
        // take first m terms of A
        vector<int> A_cut(A.begin(), A.begin() + min((int)A.size(), m));
        // R_next = R * (2 - A * R) mod x^m
        vector<int> AR = multiply(A_cut, R);
        AR.resize(m);
        vector<int> two_minus_AR(m);
        two_minus_AR[0] = (2 - AR[0] + MOD) % MOD;
        for (int i = 1; i < m; i++) {
            two_minus_AR[i] = (MOD - AR[i]) % MOD;
        }
        R = multiply(R, two_minus_AR);
        R.resize(m);
    }
    R.resize(n);
    return R;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    vector<int> Ns(T);
    int Nmax = 0;
    for (int i = 0; i < T; i++) {
        cin >> Ns[i];
        Nmax = max(Nmax, Ns[i]);
    }

    // Precompute a[k] = number of unordered labeled trees on k nodes = k^(k-1)
    vector<int> a(Nmax + 1);
    a[0] = 1;
    for (int k = 1; k <= Nmax; k++) {
        a[k] = modpow(k, k - 1);
    }

    // Build B(x) = 1 - x * (a[0] + a[1] x + ... + a[Nmax-1] x^(Nmax-1))
    // B has degree ≤ Nmax
    vector<int> B(Nmax + 1, 0);
    B[0] = 1;
    for (int i = 0; i < Nmax; i++) {
        B[i + 1] = (MOD - a[i]) % MOD;
    }

    // Compute D(x) = 1 / B(x) mod x^(Nmax+1)
    vector<int> D = invert_series(B, Nmax + 1);

    // Output the precomputed answers
    // D[n] is the number of semi-BSTs on n nodes
    for (int n : Ns) {
        cout << D[n] << "\n";
    }

    return 0;
}
