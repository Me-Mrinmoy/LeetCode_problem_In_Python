class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        last = {}
        count = {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            count[x] = count.get(x, 0) + 1

        degree = 0
        for v in count.values():
            if v > degree:
                degree = v

        ans = len(nums)
        for k, c in count.items():
            if c == degree:
                length = last[k] - first[k] + 1
                if length < ans:
                    ans = length
        return ans

if __name__ == "__main__":
    print(Solution().findShortestSubArray([1,2,2,3,1]))        # 2
    print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))    # 6
