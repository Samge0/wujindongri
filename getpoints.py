import pyautogui
import pyperclip
import time

# 初始化变量
last_position = None
last_time = 0

while True:
    current_position = pyautogui.position()
    current_time = time.time()

    # 检查是否已经过了2秒，并且坐标点有变化
    if current_position != last_position and current_time - last_time > 5:
        # 复制文本到剪贴板
        pyperclip.copy(f"{current_position.x}, {current_position.y}")
        last_position = current_position
        last_time = current_time
        print(f"Position copied to clipboard: {current_position.x}, {current_position.y}")
    else:
        print(f"Current position: {current_position.x}, {current_position.y}")

    # 为了减少CPU使用率，这里添加一个短暂的延迟
    time.sleep(0.1)