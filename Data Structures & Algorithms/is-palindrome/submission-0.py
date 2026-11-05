class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        for letter in s:
            if letter.isalnum():
                letters.append(letter.lower())
        backward = letters[::-1]
        return backward == letters
