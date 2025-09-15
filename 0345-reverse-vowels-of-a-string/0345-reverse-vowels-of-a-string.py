class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowels_inS = [v for v in s if v in vowels]
        answer = []
        for i in range(len(s)):
            
            if s[i] in vowels:
                answer.append(vowels_inS.pop())
            else:
                answer.append(s[i])
        
        return "".join(answer)