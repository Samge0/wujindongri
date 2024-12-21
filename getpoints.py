import pyautogui


while True:
    current_position = pyautogui.position()
    print(f"{current_position.x}, {current_position.y}")