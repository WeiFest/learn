import pygame,sys,random,time
from pygame.locals import *
#定义颜色变量 0=黑色  255=白色
redColor=pygame.Color(255,0,0)
blackColor=pygame.Color(0,0,0)
whiteColor=pygame.Color(255,255,255)
grayColor=pygame.Color(150,150,150)

#定义gameOver()
def gameOver(playSurface):
    gameOverFont = pygame.font.Font('arial.ttf', 72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    playSurface=pygame.display.set_mode((640,480))
    pygame.display.set_caption("贪吃蛇")

#初始化变量
snakePosition = [100,100]
snakeSegments=[[100,100],[80,100],[60,100]]
cheesePosition=[300,300]
cheeseSpawned= 1
dirction ='right'
changDirection=dirction
while True:
    #检测列如按键等pygame的事件：
    for event in pygame.event.get():
        # 从队列中获取事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key==ord('d'):
                changeDirection='right'
            if event.key == K_LEFT or event.key==ord('a'):
                changeDirection='left'
            if event.key == K_UP or event.key==ord('w'):
                changeDirection='up'
            if event.key == K_Down or event.key==ord('s'):
                changeDirection='down'
            if event.key == K_ESCAPE :
                pygame.quit()
#direction 是否正确
if changeDirection =='right' and not direction == 'left':
    direction = changeDirection
if changeDirection =='left' and not direction == 'right':
    direction = changeDirection
if changeDirection =='up' and not direction == 'down':
    direction = changeDirection
if changeDirection =='down' and not direction == 'up':
    direction = changeDirection
#根据方向移动蛇头
if direction == 'right':
    snakePosition[0] += 20
if direction == 'left':
    snakePosition[0] -= 20
if direction == 'up':
    snakePosition[0] -= 20
if direction == 'down':
    snakePosition[0] += 20

#判断是否吃掉了奶酪
if snakePosition[0]==cheesePosition[0] and snakePosition[1]==cheesePosition[1]:
    cheeseSpawned =0
else:
    snakeSeqments.pop()
if cheeseSpawned==0:
    x=random.randrange(1,32)
    y=random.randrange(1,24)
    cheesePosition=[int(x*20),int(y*20)]
    cheeseSpawned=1

playSurface.fill(blackColor)
for position in snakeSegments:
    pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))
    pygame.draw.rect(playSurface, redColour, Rect(cheesePosition[0], cheesePosition[1], 20, 20))

    pygame.display.flip()
    if snakePosition[0]>620 or snakePosition(0)<0:
        gameOver(playSurface)
    if snakePosition[1]>460 or snakePosition[1]<0:
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0]==snakeBody[0] and snakePosition[1]==snakeBody[1]:
                gamerOver(playSurface)
        fpsClock.tick(5)

if _name_ =="_main_":
 main()