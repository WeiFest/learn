import pygame
import time
import sys
import random


pygame.init()
size = width, height = [600, 400]
background_color = (0, 0, 125)
ball_color = (125, 125, 0)
rect_color = (125, 0, 0)
scores_color = (255, 255, 255)
scores_position = [500, 50]
ball_x = random.randint(20, 580)
ball_y = 20
speed_x = 1
speed_y = 1
scores = 0
point = 1
i = 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('弹弹球')
window_sign = True

while window_sign:
	screen.fill(background_color)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	mouse_x, mouse_y = pygame.mouse.get_pos()
	pygame.draw.circle(screen, ball_color, (ball_x, ball_y), 20)
	pygame.draw.rect(screen, rect_color, (mouse_x, 390, 100, 10))
	font = pygame.font.Font(None, 56)
	text = font.render(str(scores), False, scores_color)
	screen.blit(text, scores_position)
	ball_x += speed_x
	ball_y += speed_y
	if ball_x < 20 or ball_x > 580:
		speed_x = -speed_x
	if ball_y < 20:
		speed_y = -speed_y
	elif ball_y > 370:
		if mouse_x - 20 < ball_x < mouse_x + 120:
			speed_y = -speed_y
			scores += point
			i += 1
			if i % 3 == 0:
				point += point
				if speed_y > 0:
					speed_y += 1
				else:
					speed_y -= 1
				if speed_x > 0:
					speed_x += 1
				else:
					speed_x -= 1
		else:
			window_sign = False
	pygame.display.update()
	time.sleep(0.006)

pygame.quit()