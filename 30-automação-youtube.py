
import pyautogui
import os
import time
import pyperclip
import webbrowser

os.system("cls")

texto_pesquisa = "Copa do mundo"


#1 PASSO - ABRIR O NAVEGADOR E ACESSAR O SITE DO YOUTUBE
webbrowser.open("https://www.youtube.com")
time.sleep(5)

#2 PASSO - MOVER O MOUSE ATÉ A BARRA DE PESQUISA DO YOUTUBE E CLICAR
pyautogui.moveTo(665, 98, duration=5)
pyautogui.click(665, 98)

#3 PASSO - DIGITAR O TEXTO NA BARRA DE PESQUISA
pyperclip.copy(texto_pesquisa)
pyautogui.hotkey("ctrl", "v")
#pyautogui.write("Aulas Python")
pyautogui.press("enter")

#4 PASSO - CLICAR EM UM DETERMINADO VIDEO
# Scroll para cima = números positivos
# Scroll para baixo = números negativos
time.sleep(5)
pyautogui.scroll(-2700)

#5 PASSO - MOVER O MOUSE ATÉ O VIDEO E CLICAR
pyautogui.moveTo(720,791, duration=3)
pyautogui.click(720,791)

print("Você tem 5 segundos para posicionar o mouse em algum lugar da tela")
time.sleep(5)
print(f"Posição atual do mouse: {pyautogui.position()} ")