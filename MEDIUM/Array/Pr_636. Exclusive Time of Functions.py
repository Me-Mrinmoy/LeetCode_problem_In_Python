class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            func_id, typ, timestamp = log.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)
            
            if typ == "start":
                if stack:
                    # Pause the current function
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:  # "end"
                # Current function ends
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1  # move to next unit of time

        return result
