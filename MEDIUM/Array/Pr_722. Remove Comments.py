class Solution:
    def removeComments(self, source):
        in_block = False
        new_source = []
        buf = []  # temporary buffer for current line content

        for line in source:
            i = 0
            if not in_block:
                buf = []  # start a new buffer if not in a block comment

            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
                    # line comment starts → ignore rest of the line
                    break
                elif not in_block and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
                    # block comment starts
                    in_block = True
                    i += 2
                elif in_block and i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
                    # block comment ends
                    in_block = False
                    i += 2
                elif not in_block:
                    buf.append(line[i])
                    i += 1
                else:
                    # inside block comment, skip chars
                    i += 1

            # after processing the line, if we are not inside block and buffer has content → save it
            if not in_block and buf:
                new_source.append("".join(buf))

        return new_source
