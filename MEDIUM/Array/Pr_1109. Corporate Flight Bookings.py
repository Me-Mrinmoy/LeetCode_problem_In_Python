class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n + 1)
        
        for start, end, seats in bookings:
            res[start - 1] += seats
            if end < n:
                res[end] -= seats
        
        for i in range(1, n):
            res[i] += res[i - 1]
        
        return res[:n]
