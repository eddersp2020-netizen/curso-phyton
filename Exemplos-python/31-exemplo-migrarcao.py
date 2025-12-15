
import pyautogui
import time
import webbrowser
import pandas as pd
import os

# --- CONFIGURAÇÕES GLOBAIS ---
# Pequeno atraso entre cada comando para visualização e estabilidade
pyautogui.PAUSE = 0.3 
# Mover o mouse para o canto superior esquerdo (0, 0) interrompe o script
pyautogui.FAILSAFE = True 

# --- DADOS ---
# CORREÇÃO: Usamos os.path.dirname(__file__) para obter o diretório do script
# e garantimos que o arquivo 'clientes.xlsx' seja procurado na mesma pasta.
# Isso resolve o problema de "Current Working Directory".
try:
    # Obtém o caminho completo para o arquivo clientes.xlsx,
    # assumindo que ele está na mesma pasta do script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    EXCEL_FILE_PATH = os.path.join(script_dir, 'clientes.xlsx')
    
    # Carrega a planilha de clientes
    df = pd.read_excel(EXCEL_FILE_PATH)
except NameError:
    # Caso o script seja executado de forma interativa (ex: Jupyter/IDLE), __file__ não existe.
    # Neste caso, voltamos a procurar no diretório de trabalho atual.
    EXCEL_FILE_PATH = 'clientes.xlsx'
    try:
        df = pd.read_excel(EXCEL_FILE_PATH)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{EXCEL_FILE_PATH}' não foi encontrado.")
        print("Certifique-se de que o arquivo está na mesma pasta do script.")
        exit()
except FileNotFoundError:
    print(f"Erro: O arquivo '{EXCEL_FILE_PATH}' não foi encontrado.")
    print("Certifique-se de que o arquivo está na mesma pasta do script.")
    exit()

# --- COORDENADAS DO FORMULÁRIO ---
# ATENÇÃO: Estas coordenadas são APENAS EXEMPLOS.
# Cada aluno deve encontrar as coordenadas corretas para sua tela (resolução, zoom do navegador, etc.).
# Site de Teste: https://practice.expandtesting.com/register
COORD_URL = 'https://practice.expandtesting.com/register'
COORD_USERNAME = (828, 605) 
COORD_PASSWORD = (815, 689)
COORD_CONFIRM = (806, 785)
COORD_REGISTER = (874, 836)

# --- FUNÇÃO DE AUTOMAÇÃO ---
def preencher_registro(username, password):
    """Preenche o formulário de registro com os dados fornecidos."""
    
    # 1. Preencher Username
    pyautogui.moveTo(COORD_USERNAME)
    pyautogui.click()
    pyautogui.write(username)
    time.sleep(3)
    
    # 2. Preencher Password
    pyautogui.moveTo(COORD_PASSWORD)
    pyautogui.click()
    pyautogui.write(password)
    time.sleep(3)
    
    # 3. Confirmar Password
    pyautogui.moveTo(COORD_CONFIRM)
    pyautogui.click()
    pyautogui.write(password)
    time.sleep(3)
    
    # 4. Clicar em Registrar
    pyautogui.moveTo(COORD_REGISTER)
    pyautogui.click()

    # Espera um pouco para o registro ser processado
    time.sleep(3) 


#LOOP PRINCIPALpatricia.rocha
print("Iniciando a automação...")

#Abrindo o Navegador
webbrowser.open(COORD_URL)
time.sleep(5)

print("Você tem 5 segundos para posicionar o mouse")
print(f"Posição: {pyautogui.position()}")

#Executar a função preencher para cada registro do excel  
for index, linha in df. iterrows():
    #1 Passo - Pegar os dados da Planilha
    username = linha['Usuário']
    password = linha['Senha']

    #2 Passo  - Chamar a função preencher_registro
    print(f"Processando o registro: {username} ")
    preencher_registro(username, password)

print("===========================================================")
print("Automação concluida! Todos os registros foram processados!")    