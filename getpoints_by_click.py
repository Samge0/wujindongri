import pyautogui
import pyperclip
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        return  # 只关心释放鼠标按钮的事件
    if button == mouse.Button.left:
        # 复制当前双击位置的坐标点到剪贴板
        pyperclip.copy(f"{x}, {y}")
        print(f"Coordinates copied to clipboard: {x}, {y}")

def on_double_click(x, y, button, pressed):
    if pressed:
        return  # 只关心释放鼠标按钮的事件
    if button == mouse.Button.left:
        # 记录双击事件
        print(f"Double click detected at: {x}, {y}")
        on_click(x, y, button, pressed)

if __name__ == '__main__':
    with mouse.Listener(on_click=on_click, on_double_click=on_double_click) as listener:
        listener.join()