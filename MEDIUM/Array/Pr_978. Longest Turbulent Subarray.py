class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) < 2:
            return 1

        maxSum = 1
        curSum = 2
        n = len(arr)
        
        if arr[0] > arr[1]:
            switch = 1
        elif arr[0] < arr[1]:
            switch = 0
        else:
            switch = -1


        for i in range(n-1):
            if arr[i] == arr[i + 1]:
                curSum = 1
                switch = -1
            elif arr[i] > arr[i + 1] and switch == 0:
                curSum += 1
                switch = 1
            elif arr[i] < arr[i + 1] and switch == 1:
                curSum += 1
                switch = 0
            else:
                curSum = 2
                if arr[i] > arr[i + 1]:
                    switch = 1
                else:
                    switch = 0    

            maxSum = max(maxSum , curSum)

        return maxSum 
                

        
