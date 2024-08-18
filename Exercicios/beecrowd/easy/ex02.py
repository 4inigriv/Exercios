

#versão longa
A, B, C = [int(x) for x in input().strip().split(' ')]
a, b, c = A, B, C

# Verificar o maior valor
if a > b and a > c:
    primeiro = a
    if b > c: #existe a possibilidade do b ser o segundo valor maior etc
        segundo = b
        terceiro = c
    else:
        segundo = c
        terceiro = b
elif b > a and b > c:
    primeiro = b
    if a > c:
        segundo = a
        terceiro = c
    else:
        segundo = c
        terceiro = a
else:
    primeiro = c
    if a > b:
        segundo = a
        terceiro = b
    else:
        segundo = b
        terceiro = a

print(terceiro)
print(segundo) 
print(primeiro)
