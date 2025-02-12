## 无尽冬日-自动点击治疗的脚本

### 依赖
```shell
conda create -n wujindongri python=3.10.13 -y 
pip install -r requirements.txt
```

## 激活环境
```shell
conda activate wujindongri
```

### 使用

- 获取坐标点：

    - [可选] 主动右键点击屏幕拾取坐标点，默认右键点击后自动退出监听：
        ```shell
        python getpoints_by_click.py
        ```

    - [可选] 打印当前鼠标所在坐标，超过3秒自动复制当前鼠标所在坐标：
        ```shell
        python getpoints.py
        ```

- 运行自动点击脚本（例如自动点击治疗），执行前需要先配置点击的坐标信息：
    ```shell
    python main.py
    ```

### 增加自动狩猎功能
- 配置`auto_hunting.py`中需要点击的坐标组（自动狩猎一般配置4个步骤点即可），然后运行即可：
    ```shell
    python auto_hunting.py
    ```
    ![无尽冬日-自动狩猎-2](https://github.com/user-attachments/assets/9277e3c1-fda1-49b4-ab61-aa1d2fa77f2e)
