
#Age in Days
#beecrowd
entrada = int(input("Digite a idade em dias: "))

anos = entrada // 365
resto_anos = entrada % 365
meses = resto_anos // 30
dias = resto_anos % 30

# Imprima o resultado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
