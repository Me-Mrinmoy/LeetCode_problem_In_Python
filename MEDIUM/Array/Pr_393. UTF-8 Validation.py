class Solution:
    def validUtf8(self, data):
        def count_leading_ones(byte):
            count = 0
            for i in range(7, -1, -1):
                if (byte >> i) & 1:
                    count += 1
                else:
                    break
            return count

        i = 0
        n = len(data)

        while i < n:
            first_byte = data[i]
            num_bytes = count_leading_ones(first_byte)

            # Invalid if the first byte has more than 4 leading 1's or is 1 (i.e., 10xxxxxx)
            if num_bytes == 1 or num_bytes > 4:
                return False

            # If not enough bytes left
            if i + num_bytes > n:
                return False

            # Check the next num_bytes - 1 for starting with 10xxxxxx
            for j in range(1, num_bytes):
                if (data[i + j] >> 6) != 0b10:
                    return False

            # If it's a 1-byte character (starts with 0xxxxxxx)
            if num_bytes == 0:
                i += 1
            else:
                i += num_bytes

        return True
