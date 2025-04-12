#Formas de somar ate n voltando
def contar_caminhos(n):
    if n == 0:
        return 1  # caso base 
    if n < 0:
        return 0  # caso base 
    return contar_caminhos(n - 1) + contar_caminhos(n - 2) #3 - 1 -1 caminho recursivo 

