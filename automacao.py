import time
import pyautogui


def garantir_foco():
    pyautogui.click(10, 10)  
    time.sleep(1)  

pyautogui.FAILSAFE = True 

time.sleep(3)


primeiro_ponto = (958, 900)  
segundo_ponto = (342,755)


garantir_foco()


for _ in range(500):
    print(f"Movendo para o primeiro ponto: {primeiro_ponto}")
   
    pyautogui.moveTo(primeiro_ponto[0], primeiro_ponto[1], duration=0.5)
    pyautogui.click()
    time.sleep(2)

    print(f"Movendo para o segundo ponto: {segundo_ponto}")
    pyautogui.scroll(-500)  
    pyautogui.moveTo(segundo_ponto[0], segundo_ponto[1], duration=0.5)
    pyautogui.click()
    pyautogui.press('tab') 
    pyautogui.press('enter')
    time.sleep(8)
    time.sleep(0.5)
