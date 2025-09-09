class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        current = 0
        count = 0

        for i in range(len(arr)):
            current += arr[i]
            if current == target:
                count += 1
                current = 0
                if count == 2 and i < len(arr) - 1:
                    return True

        return False
