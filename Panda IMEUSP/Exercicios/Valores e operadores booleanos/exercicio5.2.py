n = int(input("Digite uma sequencia de numeros: "))

i = 0
crescente = False
decrescente = False

while not crescente and not decrescente:
    x = n % 10
    n = n // 10

    if x > (n % 10):
        crescente = True
        print("Está em ordem crescente !")
        
    else:
        decrescente = True
        print("Está em ordem decrescente !")
        
        
    
