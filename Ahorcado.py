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
        while True:
            self.mostrar_palabra()
            letra = self.obtener_letra()

            if letra in self.letras_adivinadas:
                print("Ya has adivinado esa letra. ¡Intenta con otra!")
                continue

            self.letras_adivinadas.append(letra)

            if letra in self.palabra_secreta:
                print("¡Adivinaste una letra!")
                if self.ha_ganado():
                    self.mostrar_palabra()
                    print("¡Felicidades! ¡Has ganado!")
                    break
            else:
                print("La letra no está en la palabra secreta.")
                self.intentos_restantes -= 1
                if self.intentos_restantes == 0:
                    print("¡Oh no! ¡Has perdido!")
                    print("La palabra secreta era:", self.palabra_secreta)
                    break

    def mostrar_palabra(self):
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print()

    def obtener_letra(self):
        while True:
            letra = input("Ingresa una letra: ").lower()
            if len(letra) != 1 or not letra.isalpha():
                print("Ingresa una única letra válida.")
            else:
                return letra

    def ha_ganado(self):
        for letra in self.palabra_secreta:
            if letra not in self.letras_adivinadas:
                return False
        return True

# Lista de palabras para el juego
palabras = ["python", "programacion", "videojuego", "ahorcado", "ordenador", "desarrollo"]

# Crear una instancia del juego y comenzar a jugar
juego = Ahorcado(palabras)
juego.jugar()