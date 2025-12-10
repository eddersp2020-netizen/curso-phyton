import os

os.system("cls")


def voltar_ao_menu_principal():
    input("\nPressione <Enter para voltar ao menu inicial...")
    main()

def menu():
    print("=== MENU DE OPÇÕES ===")
    print("[0] Calcular imc")
    print("[1] Sair do programa ")


def main():

    os.system("cls")
    
    menu()
    opcao = int(input("Digite uma opçao:"))

    if opcao == 0:

        nome = input("Digite seu nome: ")
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))

        imc = peso / (altura * altura)

        imc_dos_pacientes = ""

        print(f"Olá {nome}, seu IMC é: {round(imc,2)}")

        #Abaixo do peso
        if imc <= 18.5:
            print("Você está abaixo do peso")
        #Peso é normal
        elif imc >=24.9:
            print("Peso normal")
        #Sobrepeso
        elif imc <=29.9:
            print("Sobrepeso")
        #Obesidade grau I
        elif imc <=34.9:
            print("Obesidade Grau I")    
        #Obesidade grau II
        elif imc <=39.9:
            print("Obesidade Grau II")
        elif imc >=40:
            print("Obesidade Grau III")

        #Calcular dados dos pacientes
        with open("imc_dos_pacientes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome do Paciente: {nome}\n")
            arquivo.write(f"Peso do Pacinte: {peso}\n")
            arquivo.write(f"Altura do Paciente: {altura}\n")


            print("Dados salvos com sucesso!") 



        voltar_ao_menu_principal()

    else:
        input("Pressione <Enter> para sair...")
        exit()


main()