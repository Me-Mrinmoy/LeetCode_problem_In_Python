class Solution:
    def findMinDifference(self, timePoints):
        # Convert time to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            total = h * 60 + m
            minutes.append(total)
        
        # Sort minutes
        minutes.sort()
        
        # If duplicates exist, min difference is 0
        for i in range(1, len(minutes)):
            if minutes[i] == minutes[i - 1]:
                return 0
        
        # Initialize min_diff as large number
        min_diff = float('inf')
        
        # Compare adjacent time points
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)
        
        # Check circular difference (last and first across midnight)
        circular_diff = 1440 - (minutes[-1] - minutes[0])
        min_diff = min(min_diff, circular_diff)
        
        return min_diff

