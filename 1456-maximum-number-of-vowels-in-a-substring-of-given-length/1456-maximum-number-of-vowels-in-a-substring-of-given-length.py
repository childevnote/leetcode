class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        maxnum = 0
        start = 0
        end = k
        for i in range(len(s)-k+1):
            total = sum(s[start:end].count(vowel) for vowel in vowels)
            maxnum = total if total > maxnum else maxnum
            start+=1
            end+=1

        return maxnum
