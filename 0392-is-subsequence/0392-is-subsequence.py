class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True  # s가 빈 문자열이면 항상 True
        index = 0
        for w in t:
            if index < len(s) and w == s[index]:
                index += 1
        return index == len(s)
