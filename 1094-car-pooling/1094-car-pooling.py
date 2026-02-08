class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        deltas = []
        for num_passengers, fr, to in trips:
            deltas.append((fr, num_passengers))
            deltas.append((to, -num_passengers))
        
        deltas.sort()

        curr_capacity = 0
        for _, delta in deltas:
            curr_capacity += delta
            if curr_capacity > capacity:
                return False
        
        return True

