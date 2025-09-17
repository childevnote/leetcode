class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        start = 0
        end = k
        v_max = v_num = sum(s[start:end].count(vowel) for vowel in vowels)
        start, end = start + 1, end + 1
        for _ in range(start, len(s)-k+1):
            if s[start-1] in vowels:
                v_num-=1
            if s[end-1] in vowels:
                v_num+=1
            v_max = v_num if v_num > v_max else v_max
            start, end = start + 1, end + 1
        return v_max

