import pygame
from pygame.sprite import Sprite


class Alien(Sprite): # 创建一个alien类
	# 初始化外星人并设置起始位置

	def __init__(self, ai_setting, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_setting = ai_setting
		# 加载外星人图片，设置rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		# 外星人初始位置在屏幕左上角附件
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# 存储外星人的准确位置
		self.x = float(self.rect.x)

	def blit_me(self):
		# 指定位置绘制外星人
		self.screen.blit(self.image, self.rect)
