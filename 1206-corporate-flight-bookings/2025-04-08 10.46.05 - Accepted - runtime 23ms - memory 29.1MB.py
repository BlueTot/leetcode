class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        generator = [0 for _ in range(n+1)]
        for first, last, seats in bookings:
            generator[first] += seats
            if last + 1 <= n:
                generator[last + 1] -= seats
        
        prefixSum = 0
        seats = []
        for num in generator[1:]:
            prefixSum += num
            seats.append(prefixSum)
        return seats