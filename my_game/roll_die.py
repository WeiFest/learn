from collections import OrderedDict
import random

favorite_languages = OrderedDict()  # 调用模块创建一个空的有序字典
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")


class Die:			# 定义一个6面的骰子
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(random.randint(1, 6))


die_6 = Die()
for i in range(10):
	die_6.roll_die1()
