import pyautogui
import time

# 需要点击的坐标位置 - 自动狩猎 - 需要自己用getpoints_by_click.py或其他方式配置真实的坐标
click_positions = [
]

# 配置参考例子 - 自动狩猎
# click_positions = [
#     (1930, 901),
#     (2103, 1086),
#     (2101, 760),
#     (2209, 1084),
# ]

# 最大队列
MAX_QUEUE = 6

# click_positions的每个坐标的点击的间隔时间
CLICK_INTERVAL = 2

# 每轮狩猎间隔时间
HUNTING_ROUND_INTERVAL = 1 * 60

if len(click_positions) == 0:
    print("请先配置需要点击的坐标位置（main.py => click_positions）")
    exit()

# 设置鼠标移动的阈值，超过这个值将不执行点击
threshold = 50
last_position = pyautogui.position()
pause_sleep_time = 0

# 当前狩猎计数
hunting_count = 0


while True:
    
    # 遍历队列
    for i in range(MAX_QUEUE):
        print(f"自动狩猎中，当前队列：{i+1}")
        current_position = pyautogui.position()
        # 计算鼠标的移动距离
        distance = ((current_position.x - last_position.x) ** 2 + (current_position.y - last_position.y) ** 2) ** 0.5
        
        if distance < threshold:
            for position in click_positions:
                pyautogui.click(position)
                time.sleep(CLICK_INTERVAL)
        else:
            print(pause_sleep_time)
            time.sleep(pause_sleep_time)
            pause_sleep_time = 3
        
        # 更新最后的位置
        last_position = current_position
        
        # 设置一个检查间隔，减少CPU使用率
        time.sleep(0.1)
    
    # 每X分钟执行一次狩猎
    hunting_count += 1
    print(f"---------------------- 已完成第【{hunting_count}】次狩猎 ---------------------- ")
    time.sleep(HUNTING_ROUND_INTERVAL)