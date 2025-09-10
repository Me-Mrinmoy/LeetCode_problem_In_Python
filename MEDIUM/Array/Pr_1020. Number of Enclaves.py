class Solution {
public:
    int n,m;
    bool vis[505][505];
    int node;
    bool flag;

    vector<pair<int,int>> d = {{1,0},{-1,0},{0,1},{0,-1}};

    bool valid(int i,int j)
    {
        return i>=0 && i<n && j>=0 && j<m;
    }   

    void dfs(int si, int sj, vector<vector<int>>& grid)
    {
        vis[si][sj] = true;
        node++;
        for(int i=0;i<4;i++)
        {
            int ci = si + d[i].first;
            int cj = sj + d[i].second;
            if(!valid(ci,cj))
                flag = false;
            else if(!vis[ci][cj] && grid[ci][cj])
                dfs(ci,cj,grid);
        }
    }

    int numEnclaves(vector<vector<int>>& grid) {
        n = grid.size();
        m = grid[0].size();
        int ans=0;

        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(!vis[i][j] && grid[i][j])
                {
                    node = 0, flag = true;
                    dfs(i,j,grid);
                    if(flag)
                        ans += node;
                }
            }
        return ans;
    }
};
