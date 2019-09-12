import pygame, time


class Ship:

	def __init__(self, ai_setting, screen):  # 初始化飞船并设置其初始位置
		self.screen = screen
		self.ai_setting = ai_setting
		self.image = pygame.image.load("images/ship.bmp")  # 加载飞船图像并获取其外接矩形
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx  # 将每艘新飞船放在屏幕底部中央
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)			# 在飞船的属性center中存储小数值
		self.moving_right = False		# 移动标志
		self.moving_left = False

	def blit_me(self):  	# 在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)

	def update(self):		# 根据移动标志调整飞船的位置
		if self.moving_right and self.rect.right < self.screen_rect.right:		# 更新飞船的center值
			self.center += self.ai_setting.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.center -= self.ai_setting.ship_speed_factor
		self.rect.centerx = self.center		# 根据self.center更新rect对象


