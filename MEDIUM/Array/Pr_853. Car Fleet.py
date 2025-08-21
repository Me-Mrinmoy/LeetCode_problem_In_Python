class Solution:
    def carFleet(self, target, position, speed):
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)  # sort by position descending
        fleets = 0
        max_time = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > max_time:   # new fleet
                fleets += 1
                max_time = time   # update fleet time
        return fleets
