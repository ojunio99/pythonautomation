import time
import pyautogui


pyautogui.FAILSAFE = True 

time.sleep(3)


primeiro_ponto = (958, 900)  
segundo_ponto = (342,755)

for _ in range(5000):
    # Simulando Alt + D para focar na barra de endereço do navegador
    pyautogui.hotkey('alt', 'd')
    time.sleep(1)  # Aguarda 1 segundo para garantir que o foco foi mudado
    
    # Escrevendo o URL

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')  # Pressiona 'Enter' após digitar o texto
    time.sleep(3)
    # Movendo para o segundo ponto
    print(f"Movendo para o segundo ponto: {segundo_ponto}")
    pyautogui.scroll(-500)
    pyautogui.moveTo(segundo_ponto[0], segundo_ponto[1], duration=0.5)
    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    
    # Pequeno intervalo entre iterações
    time.sleep(0.5)