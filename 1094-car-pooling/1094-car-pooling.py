class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # make list of changes in capacity
        # (from, +passengers)
        # (to, -passengers)
        deltas = []
        for num_passengers, fr, to in trips:
            deltas.append((fr, num_passengers))
            deltas.append((to, -num_passengers))
        
        # sort in increasing order
        deltas.sort()

        curr_capacity = 0
        for _, delta in deltas:
            curr_capacity += delta
            if curr_capacity > capacity: # overflow
                return False
        
        return True

