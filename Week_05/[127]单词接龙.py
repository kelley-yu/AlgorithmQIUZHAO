class Solution:
    # 1. BFS
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for char in 'qazxswedcvfrtgbnhyujmkiolp':
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in wordList:
                        queue.append((new_word, step+1))
                        wordList.remove(new_word)
        return 0