class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        height,width=len(dungeon),len(dungeon[0])
        m,n=height-1,width-1

        dp=dungeon
        #princess point of place
        dp[m][n]=max(1,1-dp[m][n])
        for r in range(m-1,-1,-1):
            dp[r][n]=max(1,dp[r+1][n]-dp[r][n])
        for c in range(n-1,-1,-1):
            dp[m][c]=max(1,dp[m][c+1]-dp[m][c])
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[r][c]=max(1,min(dp[r+1][c],dp[r][c+1])-dp[r][c])
        return dp[0][0]
