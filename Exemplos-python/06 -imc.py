
#1 passo - importar a biblioteca do os
import os

#2 passo - limpar a tela do os
os.system("cls")

#3 passo- solcite a entrada
print("Exemplo imc")

peso=float(input("Digite seu peso: "))
altura=float(input("Dgite sua altura: "))

#4 passo - processamento
imc = peso / (altura * altura)

#5 passo - saída
print("seu IMC é: ",round(imc,2))