class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        addresses = set()
        def populate(s: str, curr: List[str]) -> List[str]:

            if not s and len(curr) == 4:
                addresses.add(".".join(curr))
                return
            if not s:
                return

            for i in range(1, 4):
                # in range, and has no leading zeroes
                if 0 <= int(s[:i]) <= 255 and str(int(s[:i])) == s[:i]:
                    curr.append(s[:i])
                    populate(s[i:], curr)
                    curr.pop()

        populate(s, [])
        return list(addresses)
