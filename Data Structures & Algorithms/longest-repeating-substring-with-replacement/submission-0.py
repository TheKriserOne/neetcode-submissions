class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            maxf = max(window.values())

            if r - l + 1 - maxf > k:
                window[s[l]] -= 1
                l += 1
            
        return len(s) - l 



        