class Solution:
    def valid_palindrome(self, s:str) -> bool:
        word = s.lower()
        l,r = 0, len(word) - 1

        while l < r:
            while l < r and not word[l].isalnum():
                l += 1

            while l < r and not word[r].isalnum():
                r -= 1

            if word[l] != word[r]:
                return False

            l += 1
            r -= 1

        return True

print(Solution().valid_palindrome("A man, a plan, a canal: Panama"))