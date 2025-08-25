class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        k = len(s)
        d = len(digits)

        # 1) Count numbers with fewer digits
        ans = 0
        for i in range(1, k):
            ans += d ** i

        # 2) Count numbers with same length as n
        for i in range(k):
            smaller = sum(ch < s[i] for ch in digits)
            ans += smaller * (d ** (k - i - 1))

            if s[i] not in digits:
                return ans

        # If all digits matched
        return ans + 1
