class Solution:
    def is_anagram(self, s:str, t:str):
        return sorted(s) == sorted(t)

print(Solution().is_anagram("pedro1&", "epd1r&o"))