import sys
import pygame
from bullet import Bullet


def check_events(ai_setting, screen, ship, bullets):			# 响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_setting, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def check_keydown_events(event, ai_setting, screen, ship, bullets):		# 响应按键
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:						# 创建一颗子弹，并将其加入到编组bullets中
		fire_bullet(ai_setting, screen, ship, bullets)


def check_keyup_events(event, ship):						# 松开按键
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):		# 更新屏幕上的图像，并切换到新屏幕
	screen.fill(ai_settings.background_color)  				# 每次循环重绘屏幕
	ship.blit_me()
	for bullet in bullets.sprites():						# 在飞船和外星人后面重绘所有子弹
		bullet.draw_bullet()
	pygame.display.flip() 									 # 让最近绘制的屏幕可见


def update_bullets(bullets):
	bullets.update()										# 更新子弹位置
	for bullet in bullets.copy():							# 删除消失的子弹
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# print(bullets)


def fire_bullet(ai_setting, screen, ship, bullets):
	if len(bullets) < ai_setting.bullets_allowed:			# 如果还没有到达限制，就发射一颗子弹
		new_bullet = Bullet(ai_setting, screen, ship)
		bullets.add(new_bullet)