class Solution(object):
    def numberOfLines(self, widths, s):
        lines = 1
        cur_width = 0

        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if cur_width + w > 100:
                lines += 1
                cur_width = w
            else:
                cur_width += w

        return [lines, cur_width]
