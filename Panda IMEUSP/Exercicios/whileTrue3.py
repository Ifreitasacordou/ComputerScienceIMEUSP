meuCartao = int(input("Digite o número do seu cartão de crédito: "))
cartaoLido = 1

encontreiMeuCartaoNaLista = False

while not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True
        print("Encontrei meu Caaartãoo !")
