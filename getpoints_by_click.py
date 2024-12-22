import pyperclip
from pynput import mouse
import sys  # 导入sys模块

# 是否复制坐标后自动退出
auto_exit = True

def on_click(x, y, button, pressed):
    if pressed:
        return  # 只关心释放鼠标按钮的事件
    if button == mouse.Button.right:
        # 复制当前右击位置的坐标点到剪贴板
        pyperclip.copy(f"{x}, {y}")
        print(f"Coordinates copied to clipboard: {x}, {y}")
        if auto_exit:
            return False  # 返回False来停止监听

if __name__ == '__main__':
    print("Right-click anywhere on the screen to copy the coordinates to the clipboard.")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()