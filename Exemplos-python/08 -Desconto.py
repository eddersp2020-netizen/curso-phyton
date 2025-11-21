
#1 passo - importar a biblioteca com o os
import os

#2 limpar a tela do os
os.system("cls")

print("Exemplo Desconto")
preco_original= float(input("Digite o preço: "))
porcentagem_desconto= float(input("Digite a porcentagem de desconto: "))
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"Valor do desconto: {round(valor_desconto,2)} \n")
print(f"Preço final: {round(preco_final,2)} ")
