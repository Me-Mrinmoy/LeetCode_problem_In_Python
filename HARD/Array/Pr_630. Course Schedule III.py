import heapq

class Solution:
    def scheduleCourse(self, courses):
        # Sort the courses by their end time
        courses.sort(key=lambda x: x[1])
        
        total_time = 0
        max_heap = []
        
        for duration, last_day in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)  # use negative values for max heap
            
            if total_time > last_day:
                longest_course = -heapq.heappop(max_heap)
                total_time -= longest_course
        
        return len(max_heap)
