# micro:bit V2 用 (MicroPython)。python.microbit.org で書き込む
# ・温度センサーの値を0.5秒ごとにUSBシリアルで "T:25" の形式で送る
# ・Aボタンを押すと "A" を送る
from microbit import *

count = 0
while True:
    if button_a.was_pressed():
        print("A")
    count += 1
    if count >= 25:  # 20ms x 25 = 0.5秒
        count = 0
        print("T:" + str(temperature()))
    sleep(20)
