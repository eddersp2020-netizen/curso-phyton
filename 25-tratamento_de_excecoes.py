
import os

os.system("cls")

print("Exemplos de tratamento de exceções")



try:
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    resultado = numero1 / numero2
    print(f"O resultado da divisão é {resultado}")
except ValueError as erro:
    print(f"Aconteceu o erro {erro}")
    print("Você digitou um valor ínvalido")    

