class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import collections
        if not tasks: return 0
        dic = collections.Counter(tasks)
        max_task = sorted(dic.items(), reverse=True, key = lambda x:x[1])[0][0]
        res = (dic[max_task]-1) * (n+1) + 1
        for k, v in dic.items():
            if v == dic[max_task] and k != max_task:
                res += 1
        return len(tasks) if res < len(tasks) else res