class Solution:
    # 1. DFS
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right, prev):
            if left == n and right == n:
                res.append(prev[:])
                return
            if left != n:
                helper(left+1, right, prev + '(')
            if left > right:
                helper(left, right+1, prev + ')')
        res = []
        helper(0, 0, '')
        return res

