class Solution:
    def validUtf8(self, data):
        # Number of bytes remaining to complete the current UTF-8 char
        remaining_bytes = 0

        for byte in data:
            # Consider only the last 8 bits
            byte = byte & 0xFF  

            if remaining_bytes == 0:
                # Count number of leading 1s
                mask = 0b10000000
                count = 0
                while mask & byte:
                    count += 1
                    mask >>= 1

                if count == 0:
                    continue  # 1-byte character
                if count == 1 or count > 4:
                    return False  # Invalid pattern

                remaining_bytes = count - 1  # Expect continuation bytes
            else:
                # Must be a continuation byte: starts with "10"
                if not (byte & 0b10000000 and not (byte & 0b01000000)):
                    return False
                remaining_bytes -= 1

        return remaining_bytes == 0


# Example usage:
solution = Solution()
print(solution.validUtf8([197, 130, 1]))   # True
print(solution.validUtf8([235, 140, 4]))   # False
