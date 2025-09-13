class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
# We have to sort the costs array in order of their difference
# When the difference is less we have to select the first element
# When the difference is more we have to select the second element

        n = len(costs)
        ans = 0
        l =  sorted(costs, key=lambda x:(x[0]-x[1])) # Sorting happens Here
        for i in range(n):
            if i >= n//2:
                ans += l[i][1]
            else:
                ans += l[i][0]

        return ans
