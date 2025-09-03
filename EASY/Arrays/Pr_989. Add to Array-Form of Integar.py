class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        i = len(num)-1
        while carry and i >= 0:
            a = num[i] + carry
            num[i] = a % 10
            carry = a // 10
            i -= 1
        while carry:
            num = [carry % 10] + num
            carry = carry // 10
        return num
