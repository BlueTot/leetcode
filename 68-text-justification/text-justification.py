class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        length = 0
        count = 0
        for i in range(len(words)):

            count += 1
            length += len(words[i])
            actual_length = length + count - 1
            print(i, count, length)

            if actual_length > maxWidth:

                length -= len(words[i])
                count -= 1
                if count == 1:
                    inter_width = 0
                else:
                    inter_width = (maxWidth - length) // (count - 1)
                rem = maxWidth - (length + (count - 1) * inter_width)
                s = ""
                k = 0
                print(inter_width, rem)
                for j in range(i-count, i):
                    s += words[j]
                    if j < i - 1:
                        if k < rem:
                            s += " " * (inter_width + 1)
                        else:
                            s += " " * inter_width
                    k += 1
                if count == 1:
                    s += " " * rem

                output.append(s)

                count = 1
                length = len(words[i])

        rem = maxWidth - (length + count - 1)
        output.append(" ".join(words[len(words)-count:]) + rem * " ")

        return output
