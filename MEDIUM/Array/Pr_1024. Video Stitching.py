class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort()  
        end, count, i, max_end = 0, 0, 0, 0

        while end < time:
            while i < len(clips) and clips[i][0] <= end:
                max_end = max(max_end, clips[i][1])
                i += 1
            
            if max_end == end: 
                return -1

            end = max_end  
            count += 1  

        return count
