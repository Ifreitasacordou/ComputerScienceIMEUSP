n = 113


tem = 0

while n > 0:
    x = n % 10
    n = n // 10

    if x == (n % 10):
        tem += 1       
if tem < 0:
    print("Não")
else:
    print("Sim")

    
