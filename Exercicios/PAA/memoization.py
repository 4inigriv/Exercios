# memoização
# salva os resultados para referência futura

memo = {}

def caminho_escada(n):
    if n == 0: #caso base 1
        return 1  #caso base 2
    if n < 0:
        return 0  # não existe caminho para degraus negativos
    
    if n in memo:  # se já foi calculado antes, retorna direto
        return memo[n]
    
    memo[n] = caminho_escada(n - 1) + caminho_escada(n - 2)
    return memo[n]
