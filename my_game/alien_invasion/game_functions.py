import sys
import pygame
from bullet import Bullet
from alien import Alien


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


def update_screen(ai_settings, screen, ship, aliens, bullets):		# 更新屏幕上的图像，并切换到新屏幕
	screen.fill(ai_settings.background_color)  				# 每次循环重绘屏幕
	ship.blit_me()
	# aliens.blit_me()
	aliens.draw(screen)
	for bullet in bullets.sprites():						# 在飞船和外星人后面重绘所有子弹
		bullet.draw_bullet()								# 对编组调用 draw() 时，Pygame自动绘制编组的每个元素
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


def create_fleet(ai_setting, screen, aliens):				# 创建外星人
	alien = Alien(ai_setting, screen)							# 创建一个外星人，
	number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
	#alien_width = alien.rect.width							# 外星人间距为外星人的宽度
	for alien_number in range(number_aliens_x):
		create_alien(ai_setting, screen, aliens, alien_number)
		#alien = Alien(ai_setting, screen)
		#alien.x = alien_width + 2 * alien_width * alien_number
		#alien.rect.x = alien.x
		#aliens.add(alien)


def get_number_aliens_x(ai_setting, alien_width):
	available_space_x = ai_setting.screen_width - 2 * alien_width		# 计算一行可容纳外星人的空间
	number_aliens_x = int(available_space_x / (alien_width * 2))		# 计算一行可容纳外星人数量
	return number_aliens_x


def create_alien(ai_setting, screen, aliens, alien_number):
	alien = Alien(ai_setting, screen)  # 创建一个外星人，
	alien_width = alien.rect.width  # 外星人间距为外星人的宽度
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	aliens.add(alien)


