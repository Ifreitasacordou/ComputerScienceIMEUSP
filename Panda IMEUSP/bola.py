class Bola:
    def __init__(self, cor, ci, material):
        self.cor = cor
        self.ci = ci
        self.material = material

    def trocarCor(self, cor):
        self.cor = cor

    def mostrarCor(self):
        print("A cor da bola é",self.cor)
