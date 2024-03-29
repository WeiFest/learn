import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):			# 一个对飞船发射的子弹进行管理的类
	def __init__(self, ai_setting, screen, ship):
		super(Bullet, self).__init__()		# 在飞船所处的位置创建一个子弹对象
		self.screen = screen
		self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
		# 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
		self.rect.centerx = ship.rect.centerx
		self.rect.centery = ship.rect.top
		self.y = float(self.rect.y)		# 存储用小数表示的子弹位置
		self.color = ai_setting.bullet_color
		self.speed_factor = ai_setting.bullet_speed_factor

	def update(self):					# 向上移动子弹
		self.y -= self.speed_factor		# 更新表示子弹位置的小数值
		self.rect.y = self.y			# 更新表示子弹的rect的位置

	def draw_bullet(self):				# 在屏幕上绘制子弹
		pygame.draw.rect(self.screen, self.color, self.rect)