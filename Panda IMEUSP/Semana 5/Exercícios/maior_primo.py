def éPrimo(k):
    i = 1
    divisor = 0
    while i <= k:
        if k % i == 0:
            divisor += 1
        i += 1
    if divisor == 2:
        return True
    return False


def maior_primo(num):
    i = 0
    mPrimo = 0
    while i <= num:
        if éPrimo(i)== True:
            mPrimo = i
        i+=1        
    return mPrimo
    
