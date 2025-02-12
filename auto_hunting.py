import pyautogui
import time

# 需要点击的坐标位置 - 自动狩猎 - 需要自己用getpoints_by_click.py或其他方式配置真实的坐标
click_positions = [
]

# click_positions配置参考例子
# click_positions = [
#     (1930, 901),
#     (2103, 1086),
#     (2101, 760),
#     (2209, 1084),
# ]

# 最大队列
MAX_QUEUE = 6

# click_positions的每个坐标的点击的间隔时间，如果网络加载慢或者卡顿，这里应该适当调大
CLICK_INTERVAL = 2

# 每轮狩猎间隔时间
HUNTING_ROUND_INTERVAL = 1 * 60

if len(click_positions) == 0:
    print("请先配置需要点击的坐标位置（main.py => click_positions）")
    exit()

# 提取所有 x 坐标
x_coords = [position[0] for position in click_positions]

# 设置鼠标移动的阈值，默认为x坐标方向的最大值减去最小值，再加个浮动值10
THRESHOLD = max(x_coords) - min(x_coords) + 10


if __name__ == '__main__':
    # 最后一次坐标的x值
    last_position_x = 0
    # 当前鼠标坐标x值
    current_position_x = 0
    # 鼠标变动后的等待时间
    pause_sleep_time = 0

    # 当前狩猎计数
    hunting_count = 0

    while True:
        # 遍历队列
        for i in range(MAX_QUEUE):
            print(f"自动狩猎中，当前队列：{i+1}")
            
            if current_position_x != 0:
                # 只有当前鼠标x坐标有值时，才进行判断，因为存在其他地方点击运行，那时候的鼠标位置还不在目标范围内
                current_position_x = pyautogui.position().x
                # 计算鼠标的移动距离 - 这里默认仅计算x轴方向差值
                distance = abs(current_position_x - last_position_x)
            else:
                distance = 0
            
            if distance < THRESHOLD:
                for position in click_positions:
                    pyautogui.click(position)
                    if current_position_x == 0:
                        current_position_x = position[0]
                    time.sleep(CLICK_INTERVAL)
            else:
                print(f"鼠标x轴横向移动距离 {distance} 大于预设阈值 {THRESHOLD}, 取消当前点击操作")
                time.sleep(pause_sleep_time)
                pause_sleep_time = 3
            
            # 更新最后的位置
            last_position_x = current_position_x
        
        # 每X分钟执行一次狩猎
        hunting_count += 1
        print(f"---------------------- 已完成第【{hunting_count}】次狩猎 ---------------------- ")
        time.sleep(HUNTING_ROUND_INTERVAL)