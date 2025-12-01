

def somar(numero01, numero02):
    resultado = numero01 + numero02
    print(f"A Soma é: {resultado}")

def subtrair(numero01, numero02):
    resultado = numero01 - numero02
    print(f"A Subtração é: {resultado}")

def dividir(numero01, numero02):
    resultado = numero01 / numero02
    print(f"A Divisão é: {resultado}")

def multiplicar(numero01, numero02):
    resultado = numero01 * numero02
    print(f"A Multiplicação é: {resultado}")

def imprimir_msg_erro():
    print("Opção Inválida!")

def calcular_resto_divisao(numero01, numero02):
    resultado = numero01 % numero02
    print(f"O RESTO da divisão é: {resultado}")  

def somar_com_retorno(numero01, numero02):
    resultado = numero01 + numero02
    return resultado

def subtrair_com_retorno(numero01, numero02):
    resultado = numero01 - numero02
    return resultado

def exibir_menu():
    print("==================================")
    print("Selecione uma opção abaixo")
    print("[1] - Soma")
    print("[2] - Subtração")
    print("[3] - Divisão")
    print("[4] - Multiplicação")
    print("[5] - Resto da Divisão")

