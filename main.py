import pyautogui
import time

# 设置鼠标移动的阈值，超过这个值将不执行点击
threshold = 50
last_position = pyautogui.position()
pause_sleep_time = 0

while True:
    current_position = pyautogui.position()
    # 计算鼠标的移动距离
    distance = ((current_position.x - last_position.x) ** 2 + (current_position.y - last_position.y) ** 2) ** 0.5
    
    if distance < threshold:
        pyautogui.click(2440, 1226)
    else:
        print(pause_sleep_time)
        time.sleep(pause_sleep_time)
        pause_sleep_time = 3
    
    # 更新最后的位置
    last_position = current_position
    
    # 设置一个检查间隔，减少CPU使用率
    time.sleep(0.1)