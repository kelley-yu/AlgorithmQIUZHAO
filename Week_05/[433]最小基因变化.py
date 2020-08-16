class Solution:
    # BFS
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = collections.deque([(start, 0)])
        while queue:
            word, step = queue.popleft()
            if word == end:
                return step
            for i in range(len(word)):
                for char in 'ACGT':
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in bank:
                        queue.append((new_word, step+1))
                        bank.remove(new_word)
        return -1