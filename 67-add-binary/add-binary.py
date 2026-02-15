class Solution:
    def addBinary(self, a, b):
        m = len(a) - 1
        n = len(b) - 1
        
        result = []
        carry = 0

        while m >= 0 or n >= 0:
            total = carry

            if m >= 0:
                total += ord(a[m]) - ord('0')
                m -= 1

            if n >= 0:
                total += ord(b[n]) - ord('0')
                n -= 1

            result.append('0' if total % 2 == 0 else '1')
            carry = total // 2

        if carry:
            result.append('1')

        return ''.join(result[::-1])
