
import os

#Limpando a tela
os.system("cls")

# Exemplo de função sem parametros
def escreva():
     print("Olá mundo!")

#Exemplo de função com parametros
def exibir_idade(suaidade, nome):
    print(f"Seu nome é {nome}, você tem {suaidade} anos!")

def somar(n1,n2):
        resultado = n1 + n2
        print(f"O resultado é: {resultado}")

# Exemplo de função com retorno
def subtrair(valor1,valor2):
    resultado = valor1 - valor2
    return resultado        
        

print("Executou o Programa")


# Chamando uma função sem parametros
escreva()

# Chamando uma função com parametros
exibir_idade(17, "Maria")
exibir_idade(28, "Joao")
somar(50,90)


# Chamando uma Funçao com retorno
print(f"A subtração é: {subtrair(5,2)}")