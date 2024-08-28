while True:
    k = int(input())  # valor k 
    if k == 0:  # termina se k for 0
        break
    
    n, m = map(int, input().split())  # coordenadas do ponto divisório
    
    for i in range(k):
        x, y = map(int, input().split())  # coordenadas da consulta
        
        if x == n or y == m:
            print("divisa")
        elif x > n and y > m:
            print("NE")  # Nordeste
        elif x < n and y > m:
            print("NO")  # Noroeste
        elif x > n and y < m:
            print("SE")  # Sudeste
        elif x < n and y < m:
            print("SO")  # Sudoeste
