from collections import deque

class Solution:

    def next_turn(self, turn, state):
        i = turn
        while True:
            i = (i + 1) % len(state)
            if state[i] != "*":
                return i

    def predictPartyVictory(self, senate: str) -> str:
        queue = deque([(0, 0, senate)])
        while queue:
            turn, r, state = queue.popleft()
            if len(set(rep := state.replace("*", ""))) == 1:
                return "Radiant" if rep[0] == "R" else "Dire"
            i = turn
            while True:
                i = (i + 1) % len(state)
                if state[i] != state[turn] and state[i] != "*":
                    new_state = state[:i]+"*"+state[i+1:]
                    nt = self.next_turn(turn, new_state)
                    nr = r+1 if nt <= turn else r
                    queue.append(s := (nt, nr, new_state))
                    break
