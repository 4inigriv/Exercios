class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = len(s) - 1  # Começa no último índice da string

        # Ignorar espaços no final da string
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Contar os caracteres do último palavra
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count
