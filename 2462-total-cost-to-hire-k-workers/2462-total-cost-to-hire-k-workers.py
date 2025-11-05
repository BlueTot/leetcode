from heapq import heappush, heappop, heapify

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        workers = [(n, 0) for n in costs[:candidates]] + [(n, 1) for n in costs[-candidates:]]
        heapify(workers)

        total = 0
        head, tail = candidates, len(costs)-candidates-1
        for _ in range(k):
            choice, start = heappop(workers)
            total += choice
            if start == 0:
                if 0 <= head < len(costs) and head <= tail:
                    heappush(workers, (costs[head], 0))
                    head += 1
            else:
                if 0 <= tail < len(costs) and head <= tail:
                    heappush(workers, (costs[tail], 1))
                    tail -= 1
            print(choice, head, tail)
        
        return total

        