class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        decrypted = [0 for _ in range(len(code))]
        length = len(code)

        if k > 0:
            for i in range(length):
                num = 0
                for j in range(1, k+1):
                    num += code[(i+j) % length]
                decrypted[i] = num

        elif k < 0:
            for i in range(length):
                num = 0
                for j in range(1, abs(k) + 1):
                    num += code[(i-j) % length]
                decrypted[i] = num
        return decrypted
