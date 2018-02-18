def main():
    x = 1
    y = 2
    
    
    
    def fatorial(num):
        i = num
        f = 1
        while i >= 1 :
            f *= i
            i -= 1
        return f

    def combinacao(m,n):
        return fatorial(m) / (fatorial(m - n) * fatorial(n))

    combinacao(x,y)

