class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S) }
        left = right = 0
        res = []
        for i, c in enumerate(S):
            right = max(right, last[c])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res
