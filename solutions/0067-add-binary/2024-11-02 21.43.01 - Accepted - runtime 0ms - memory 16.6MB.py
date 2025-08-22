class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        carry = 0
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))
        for b1, b2 in zip(a[::-1], b[::-1]):
            output += str((r := int(b1) ^ int(b2)) ^ carry)
            carry = int(b1) & int(b2) | r & carry
        if carry == 1:
            output += str(carry)
        return output[::-1]