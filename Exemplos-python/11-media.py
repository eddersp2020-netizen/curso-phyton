import os

os.system("cls")

print("""
      
██████╗░░█████╗░██╗░░░░░███████╗████████╗██╗███╗░░░███╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██║████╗░████║
██████╦╝██║░░██║██║░░░░░█████╗░░░░░██║░░░██║██╔████╔██║
██╔══██╗██║░░██║██║░░░░░██╔══╝░░░░░██║░░░██║██║╚██╔╝██║
██████╦╝╚█████╔╝███████╗███████╗░░░██║░░░██║██║░╚═╝░██║
╚═════╝░░╚════╝░╚══════╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝
      """)

resposta = "sim"

while(resposta == "sim"):

    nome = input("Digite o nome do aluno: ")
    nota01 = float(input("Digite a primeira nota: "))
    nota02 = float(input("Digite a segunda nota: "))
    nota03 = float(input("Digite a terceira nota: "))

    media = (nota01 + nota02 + nota03) / 3

    situacao_do_aluno = ""

    #Mostrando a média
    print(f"Sua média foi {round(media,2)}")

    #Verificando se o aluno está aprovado
    if media >=7:
        print("Aprovado")
        situacao_do_aluno = "Aprovado"
    elif media >=4:
        print("Recuperação")
        situacao_do_aluno = "Recuperação"
    else: 
        print("Reprovado")
        situacao_do_aluno = "Reprovado"

    #Gravar os dados dos alunos
    with open("notas_dos_alumos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome do Aluno: {nome}\n")
        arquivo.write(f"Nota 01: {nota01}\n")
        arquivo.write(f"Nota 02: {nota02}\n")
        arquivo.write(f"Nota 03: {nota03}\n")
        arquivo.write(f"Média do aluno: {media}\n")
        arquivo.write(f"Situação do aluno: {situacao_do_aluno}\n")
        arquivo.write("========================================================= \n")

        print("Dados salvos com sucesso!")


    resposta = input("Gostaria de executar novamente, sim ou não?:")

    os.system("cls")    

input("Pressione qualquer <Enter> para fecha o programa.")