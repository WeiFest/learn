"""
一个简单的2d小游戏测试
"""
import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions
from bullet import Bullet
from pygame.sprite import Group

# sys.path.append('D:/Python_Pycharm/python_learn/alien_invasion')


def run_game():												# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting .screen_height))
	pygame.display.set_caption("外星人入侵")
	# background_color = ai_setting.background_color		# 设置背景颜色
	ship = Ship(ai_setting, screen)
	bullets = Group()										# 创建一个用于存储子弹的编组
	# bullet = Bullet(ai_setting, screen, ship)
	while True:  # 开始游戏的主循环
		game_functions.check_events(ai_setting, screen, ship, bullets)
		ship.update()
		game_functions.update_bullets(bullets)
		game_functions.update_screen(ai_setting, screen, ship, bullets)


run_game()