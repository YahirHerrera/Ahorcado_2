import random

class Ahorcado:
    def __init__(self, palabras):
        self.palabras = palabras
        self.palabra_secreta = random.choice(palabras)
        self.letras_adivinadas = []
        self.intentos_restantes = 6

    def jugar(self):
        print("Hola bienvenido este es un ahorcado")
        print("Tendras que adivinar la palabra letra por letra")
        print("OJO cuidado solo contaras con un limite de intentos en este caso son 6")