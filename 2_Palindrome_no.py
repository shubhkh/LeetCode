class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        originalX = x
        numrev = 0

        while x > 0:
            lastdig = x % 10
            numrev = numrev * 10 + lastdig
            x = x // 10

        return numrev == originalX
