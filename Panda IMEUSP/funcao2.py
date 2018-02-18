#Depois de criar a classe e as caracteristica
#instanciar o objeto

def main():
    carro1 = Carro('Fusca', 1900, 'azul', 90)
    carro2 = Carro('Brasilia', 1900, 'amarela', 85)

    carro1.acelerar(100)
    carro2.acelerar(86)
    
    carro1.pare()
    carro2.pare()

class Carro:
    def __init__(self, modelo, ano, cor, vm):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.vm = vm
        self.vel = 0

    def acelerar(self, velocidade):
        self.vel = velocidade
        self.imprima()

    def imprima(self):
        if self.vel == 0:
            print(self.modelo, self.ano, self.cor)
        elif self.vel > self.vm:
            print(self.modelo, self.cor,"está indo, muito rápido !")
        else:
            print(self.modelo,self.cor,"está indo a", self.vel,"Km/h !")
            
    def pare(self):
        self.vel = 0
        self.imprima()

main()

        
