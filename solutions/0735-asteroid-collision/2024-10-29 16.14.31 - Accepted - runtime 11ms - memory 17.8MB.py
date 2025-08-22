class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            stack.append(num)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                if abs(stack[-2]) > abs(stack[-1]):
                    stack.pop()
                elif abs(stack[-2]) < abs(stack[-1]):
                    stack.pop(-2)
                else:
                    stack.pop()
                    stack.pop()
        return stack