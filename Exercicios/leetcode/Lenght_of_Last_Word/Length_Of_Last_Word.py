class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        for char in s[::-1]:
            if char != ' ':
                count += 1
            else:
                if count > 0:
                    # Quando encontra um espaço significa que terminou a palavra
                    break
        return count
