from collections import deque
class Solution:
    vals = {2 : (128+64+32, 128+64), 3 : (128+64+32+16, 128+64+32), 4:(128+64+32+16+8, 128+64+32+16)}
    def valid_utfn(self, n, data):
        if len(data) == 1:
            return data[0] & 128 == 0
        for i, num in enumerate(data):
            if i == 0:
                if num & self.vals[len(data)][0] != self.vals[len(data)][1]:
                    return False
            else:
                if num & 192 != 128:
                    return False       
        return True

    def validUtf8(self, data: List[int]) -> bool:
        queue = deque([0])
        visited = set()
        data = [i & 255 for i in data]
        while queue:
            i = queue.popleft()
            if i == len(data):
                return True
            if i not in visited:
                visited.add(i)
                for size in range(1, 5):
                    if i+size <= len(data) and self.valid_utfn(size, data[i:i+size]):
                        queue.append(i+size)
        return False
            
        
        