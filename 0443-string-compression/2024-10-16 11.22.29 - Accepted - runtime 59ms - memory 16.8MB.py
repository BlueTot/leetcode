class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        prev_char = None
        index = 0
        s = []
        for index, char in enumerate(chars):
            if prev_char is None:
                prev_char = char
                i = index
            elif prev_char != char:
                s.append(prev_char)
                if index - i != 1:
                    for c in str(index - i):
                        s.append(c)
                i = index
                prev_char = char
        s.append(prev_char)
        if len(chars) - i != 1:
            for c in str(len(chars) - i):
                s.append(c)
        for index, ch in enumerate(s):
            chars[index] = ch
        return len(s)

