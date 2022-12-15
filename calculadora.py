
class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(numero1, numero2):
        somando = numero1 + numero2
        print(f"O Resultado da soma dos valores é: {somando}")

    def subtracao(numero1, numero2):
        subtraindo = numero1 - numero2
        print(f"O Resultado da subtração dos valores é: {subtraindo}")

    def multiplica(numero1, numero2):
        multiplicando = numero1 * numero2
        print(f"O Resultado da multiplicação dos valores é: {multiplicando}")

    def divide(numero1, numero2):
        dividindo = numero1 / numero2
        print(f"O Resultado da divisão dos valores é: {dividindo:.2f}")
