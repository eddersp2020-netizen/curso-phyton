
import os
os.system("cls")

try:
    numero = int(input("Digite um numero interiro: "))
    resultado = 10 / numero

except ZeroDivisionError:
    print("Erro: não é possivel dividir por zero.")

except ValueError:
    print("Erro: você não digitou u número valido.")

else:
    # Executa apenas se **nenhuma exceção** tiver ocorrido
    print(f"O resultado da divião é: {resultado}")
finally:
    # Executa sempre, indeoendente de erro ou sucesso
    print("Encerrando a operação...")                

