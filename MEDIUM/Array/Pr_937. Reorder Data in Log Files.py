class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest, identifier, log))

        # Sort by content, then identifier
        letter_logs.sort(key=lambda x: (x[0], x[1]))

        return [log for _, _, log in letter_logs] + digit_logs
