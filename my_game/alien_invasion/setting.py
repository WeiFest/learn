"""
用来存储《外星人入侵》的所有设置的类
"""


class Settings:
	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600
		self.background_color = (230, 230, 230)
		self.ship_speed_factor = 1.5		# 飞船的速度设置

		self.bullet_width = 2
		self.bullet_height = 5
		self.bullet_speed_factor = 0.2		# 子弹的速度设置
		self.bullet_color = (0, 0, 255)
		self.bullets_allowed = 10			# 子弹的最大数量设置
