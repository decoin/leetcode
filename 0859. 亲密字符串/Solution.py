class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) != len(A):
            return True
        a = []
        b = []
        for i in range(len(A)):
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
        if len(a) == len(b) == 2 and a == b[::-1]:
            return True
        else:
            return False
