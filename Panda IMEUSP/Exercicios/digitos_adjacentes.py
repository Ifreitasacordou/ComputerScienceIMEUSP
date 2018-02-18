n = int(input("Digite um número inteiro: "))

adjacente = 0

while n > 0:
    x = n % 10
    n = n // 10

    if x == (n % 10):
        adjacente += 1
if adjacente < 1:
    print("não")
else:
    print("sim")
