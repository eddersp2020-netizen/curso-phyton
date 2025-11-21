

#1 passo -importar a biblioteca com o os
import os


#2 passo - limpar a tela do os
os.system("cls")

#3 passo - socilitar entrada
print("--------------")

valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
soma=valor1 + valor2
sub=valor1 - valor2
multi=valor1 * valor2
div=valor1 / valor2

print(f"A soma é: {soma} | A subtração é: {sub} | A divisão é: {div} | A multiplicação é: {multi}")
