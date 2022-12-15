from calculadora import Calculadora

def pergunta_inical():
    inicial = int(input("Qual operação deseja executar? \n"
                    "1. Soma:  \n"
                    "2. Subtração: \n"
                    "3. Multiplicação: \n"
                    "4. Divisão \n"))

    if inicial == 1:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        Calculadora.soma(numero1, numero2)

    elif inicial == 2:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        Calculadora.subtracao(numero1, numero2)

    elif inicial == 3:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        Calculadora.multiplica(numero1, numero2)

    elif inicial == 4:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        Calculadora.divide(numero1, numero2)

    else:
        print("Digite uma opção válida:")



