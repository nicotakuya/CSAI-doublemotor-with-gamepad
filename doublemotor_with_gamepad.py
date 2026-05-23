# ゲームパッドでダブルモーターを動かす
# (1)電源を入れる。
# (2)接続カードを読み込む。
# (3)ボタンを押して接続待機状態にする（ボタンが点滅）。

# pygameのインストールで失敗する場合、pygame-ceを使う。

import tkinter as tk
from tkinter import messagebox
import legoeducation as le
import pygame
import sys

# 接続カードの情報を設定
card_color = le.LEGO_COLOR_RED  # 動作環境に合わせて修正
card_serial = '1309'            # 動作環境に合わせて修正

SPEEDMAX = 30    # モーター最大速度
THRESHOLD = 0.25 # レバーのしきい値
TIMMING = 20     # コマンドの送信間隔[フレーム]

# DoubleMotor
doublemotor = le.DoubleMotor()

# Connect 処理
try:
    print('Connecting...')
    doublemotor.connect(
        card_color=card_color, card_serial=card_serial
    )
except Exception as e:
    print('Error:'+str(e))

if doublemotor.connected:
    print('Connected')
else:
    print('Connection Failed')
    sys.exit()

# pygame 初期化
pygame.init()
pygame.joystick.init()

# ゲームパッドの確認
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("ゲームパッドが接続されていません。")
    pygame.quit()
    sys.exit()

# 1台目のゲームパッドを使用
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"接続されているゲームパッド: {joystick.get_name()}")

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32)
text_color = (0, 0, 0)
line_color = (0, 0, 128)

speed_left_old = 0
speed_right_old = 0
loopcnt = 0
# メインループ
endflag = False
while endflag != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            endflag = True
        
        # ボタンが押されたときの処理
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"ボタン {event.button} が押されました")

    # ゲームパッドの入力
    axis_x = joystick.get_axis(0) # 左レバーX軸(-1.0 ~ +1.0)
    axis_y = joystick.get_axis(1) # 左レバーY軸(-1.0 ~ +1.0)

    screen.fill("white")

    text = 'AXIS X : {:.3f}'.format(axis_x)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (80, 50))

    text = 'AXIS Y : {:.3f}'.format(axis_y)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (80, 50+40))

    cx = 320
    cy = 240
    pygame.draw.line(screen, line_color, (cx,cy-100), (cx,cy+100), width=1)
    pygame.draw.line(screen, line_color, (cx-100,cy), (cx+100,cy), width=1)
    sx = cx+int(100*axis_x)
    sy = cy+int(100*axis_y)
    radius = 20
    pygame.draw.circle(screen, "red", (sx,sy), radius)

    if loopcnt==0:
        speed_left = 0 
        speed_right = 0
        if abs(axis_y) > THRESHOLD:
            speed_left = -SPEEDMAX * axis_y
            speed_right = -SPEEDMAX * axis_y

        if abs(axis_x) > THRESHOLD:
            speed_left = SPEEDMAX * axis_x
            speed_right = -SPEEDMAX * axis_x

        # 速度が変化した場合、コマンド送信
        if speed_left_old != speed_left or speed_right_old != speed_right:
            doublemotor.movement_move_tank(speed_left, speed_right)

        # モーターの速度をバックアップ
        speed_left_old = speed_left
        speed_right_old = speed_right

    pygame.display.flip()
    loopcnt = (loopcnt+1) % TIMMING
    clock.tick(60) # 60 FPS
#
doublemotor.disconnect()
pygame.quit()