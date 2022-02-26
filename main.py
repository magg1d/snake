import pygame
pygame.init()

if True:
    WIDTH, HEIGHT = 600, 600

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    FPS = 30

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    LIGHT_BLUE = (0, 255, 255)
    PURPLE = (255, 0, 255)

FONT_SIZE = 20
SCALE = WIDTH//20

class Snake():
    VELO = 5
    COLOR = WHITE

    def __init__(self):
        self.headx = WIDTH//2
        self.heady = HEIGHT//2
        self.xvel = self.VELO
        self.yvel = 0
        self.headwidth = SCALE
        self.headheight = SCALE

    def move(self, dir):
        if dir == 0:
            self.xvel = 0
            self.yvel = self.VELO
            self.heady += self.yvel
        elif dir == 1:
            self.xvel = self.VELO
            self.yvel = 0
            self.headx += self.xvel
        elif dir == 2:
            self.xvel = 0
            self.yvel = -1*self.VELO
            self.heady += self.yvel
        elif dir == 3:
            self.xvel = -1*self.VELO
            self.yvel = 0
            self.headx += self.xvel
        else:
            return

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.headx, self.heady, self.headwidth, self.headheight))
        pygame.display.update()
        

def draw(win):
    win.fill(BLACK)
    pygame.display.update()


def handle_snake_movement(keys, snake):
    if keys[pygame.K_UP] and snake.yvel == 0: #and left_paddle.y - left_paddle.VEL >= 0:
        snake.move(0)
    if keys[pygame.K_RIGHT] and snake.xvel == 0: #and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        snake.move(1)
    if keys[pygame.K_DOWN] and snake.yvel == 0: #and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        snake.move(2)
    if keys[pygame.K_LEFT] and snake.xvel == 0: #and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        snake.move(3)

def main():
    run = True
    clock = pygame.time.Clock()

    snake = Snake()

    while run:
        clock.tick(FPS)
        snake.draw(WIN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        key = pygame.key.get_pressed()
        handle_snake_movement(key, snake)

    pygame.quit()

main()