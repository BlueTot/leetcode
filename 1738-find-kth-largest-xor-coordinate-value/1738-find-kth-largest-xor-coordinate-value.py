from heapq import heappush, heappop

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:

        m, n = len(matrix), len(matrix[0])
        min_heap = []

        # we use the 2D prefix sum formula
        # A[i,j] = A[i-1,j] + A[i,j-1] - A[i-1][j-1] + M[i,j]
        # in this case + is XOR and - is the inverse of XOR which is also XOR
        
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i-1][j] ^ matrix[i][j-1] ^ matrix[i-1][j-1]
                elif i == 0 and j > 0:
                    matrix[i][j] ^= matrix[i][j-1]
                elif j == 0 and i > 0:
                    matrix[i][j] ^= matrix[i-1][j]
                
                # update top k heap
                if len(min_heap) < k:
                    heappush(min_heap, matrix[i][j])
                elif len(min_heap) == k and matrix[i][j] > min_heap[0]:
                    heappop(min_heap)
                    heappush(min_heap, matrix[i][j])

        return heappop(min_heap)
