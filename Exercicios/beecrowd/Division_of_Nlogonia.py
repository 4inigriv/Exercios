while True:
    n, m = map(int, input().split()) #numero de compraçao da nova divisao
    if n == 0 or m == 0:
        break  # Sai do loop se o usuário inserir 0 0
    x, y = map(int, input().split()) #coordenadas das cidades 

    #o problema é um plano cartesiano mt simples
    if x == n or y == m: #está na divisão
        print("divisa")
    elif x > n and y > m:
        print("NE")  # Nordeste
    elif x < n and y > m:
        print("NO")  # Noroeste
    elif x > n and y < m:
        print("SE")  # Sudeste
    elif x < n and y < m:
        print("SO")  # Sudoeste
