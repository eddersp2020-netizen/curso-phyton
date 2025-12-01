
import os

#limpar a tela
os.system("cls")

#Importar as funcoes
import funcoes_da_calculadora as funcoes

resposta = "sim"

while resposta == "sim":

    os.system("cls")


    print("Calculadora com Funções")

    numero01 = float(input("Digite o primeiro número: "))
    numero02 = float(input("Digite o segundo número: "))

    #Mostrando as opções
    funcoes.exibir_menu()
    

    opcao = input("Escolha uma opção: ")

    #Verificar a opção escolhida
    if opcao == "1":
        #somar(numero01, numero02)
        print(f"A soma: {funcoes.somar_com_retorno(numero01, numero02)}")
    elif opcao == "2":
        print(f"A sub: {funcoes.subtrair_com_retorno(numero01, numero02)}")
    elif opcao == "3":
        funcoes.dividir(numero01, numero02)
    elif opcao == "4":
        funcoes.multiplicar(numero01, numero02)
    elif opcao == "5":
        funcoes.calcular_resto_divisao(numero01, numero02)
    else:
        funcoes.imprimir_msg_erro()

    resposta = input("Dejesa executar novamente? (sim ou não): ").lower()

print("Programa encerrado com sucesso!")

