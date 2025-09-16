class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        def find_target(left, right, target, is_upside):
            while left <= right:
                mid = (left + right) // 2
                mid_val = mountain_arr.get(mid)

                if mid_val == target:
                    return mid
                
                if is_upside:
                    if target > mid_val:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if target > mid_val:
                        right = mid - 1
                    else:
                        left = mid + 1

            return -1

        def find_peak():
            nonlocal length

            left, right = 0, length - 1

            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            
            return left

        peak_index = find_peak()


        result = find_target(0, peak_index, target, True)
        if result != -1:
            return result
        
        return find_target(peak_index + 1, length - 1, target, False)        
