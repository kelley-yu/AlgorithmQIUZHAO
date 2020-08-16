class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = '#'
        def dfs(i, j, node, pre, seen):
            if '#' in node:
                res.add(pre)
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_i, new_j = i+di, j+dj
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] in node and (new_i, new_j) not in seen:
                    dfs(new_i, new_j, node[board[new_i][new_j]], pre+board[new_i][new_j], seen | {(new_i, new_j)})
        res = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)