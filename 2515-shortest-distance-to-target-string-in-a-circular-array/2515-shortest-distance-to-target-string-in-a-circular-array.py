class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        for i in range(len(words)):
            left = (startIndex - i) % len(words)
            right = (startIndex + i) % len(words)
            if words[left] == target or words[right] == target:
                return i
        
        return -1
