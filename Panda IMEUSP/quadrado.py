class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado
        return tamanho_lado

    def area(self, tamanho_lado):
        area = (self.tamanho_lado ** 2)
        return area
        
