numero = int(input("Digite uma sequência de números: "))

##numeroadjacente = False
c = 0
while numero > 0:
        
    x = numero % 10
    numero = numero // 10
    if x == (numero % 10):
##        numeroadjacente = True
        c += 1
if c != 0:
    print("Há quantidade de números adjacentes é: ", c)
else:
    print("Nao há números adjacentes")

        
        
        
        
         
         
    

    
