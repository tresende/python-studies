#arquivo modelos.py

class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)
        self.curtidas = 0

    def imprime(self):
        imc = self.peso / (self.altura **2)
        print 'O IMC de %s é: %s ' %(self.nome, imc)