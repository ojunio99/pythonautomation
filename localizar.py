import pyautogui

while True:
    x, y = pyautogui.position()
    print(f"Posição do rato: {x}, {y}", end="\r")  # Atualiza no terminal
