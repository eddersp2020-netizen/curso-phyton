
#1 passo - importar a biblioteca do os
import os

#2 passo - limpar a tela com o os
os.system ("cls")

print("Calcule a porcentagem")

#3 passo - solicite a entrada
valor1 = int(input("Digite o primeiro valor: "))
porcentagem = int(input("Digite o segundo valor: "))

#4 passo - processamento
resultado = valor1 * (porcentagem /100)

#5 passo - saída
print(f"A porcentagem é: {resultado}")


