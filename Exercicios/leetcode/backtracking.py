def contar_caminhos(n):
    if n == 0:
        return 1  # 1 forma de somar "nada"
    if n < 0:
        return 0  # não tem forma de somar a um número negativo
    return contar_caminhos(n - 1) + contar_caminhos(n - 2)
