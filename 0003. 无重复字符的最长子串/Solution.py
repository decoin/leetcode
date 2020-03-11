class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        substr = set()
        maxlen = 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            if len(substr) > maxlen:
                maxlen = len(substr)
        return maxlen
