class Solution:
    def isSelfCrossing(self, distance):
        for i in range(3, len(distance)):
            # Case 1
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # Case 2
            if i >= 4:
                if distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                    return True
            # Case 3
            if i >= 5:
                if (distance[i-2] >= distance[i-4] and
                    distance[i] + distance[i-4] >= distance[i-2] and
                    distance[i-1] <= distance[i-3] and
                    distance[i-1] + distance[i-5] >= distance[i-3]):
                    return True
        return False
