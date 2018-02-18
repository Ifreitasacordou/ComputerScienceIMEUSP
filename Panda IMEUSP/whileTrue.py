decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))


while decrescente:
    valor = int(input("Digite um número da sequência: "))
    if valor > anterior:
        decrescente = False
    else:
        anterior = valor
