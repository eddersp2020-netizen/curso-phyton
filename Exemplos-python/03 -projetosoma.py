
#1 passo - importar a biblioteca do os
import os

#2 passo - limpar a tela com o os
os. system("cls")

print("""
████████████████████████████████████████████████████████████████████
█▄─▄▄─█▄─▄▄▀█─▄▄─███▄─▄█▄─▄▄─█─▄─▄─█─▄▄─███─▄▄▄▄█─▄▄─█▄─▀█▀─▄██▀▄─██
██─▄▄▄██─▄─▄█─██─█─▄█─███─▄█▀███─███─██─███▄▄▄▄─█─██─██─█▄█─███─▀─██
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀""")
print("------------------------")

#3 passo - Solicitar as entradas
numero_1 = int(input("Digite o primeiro número: "))
numero_2 =int(input("Digite o segundo número: "))

#4 passo - processamento
resultado = numero_1 + numero_2

#5 passo - saída - mostrar o resultado
print(f"O resultado da soma é: {resultado}")

input("Pressione uma tecla para fechar")