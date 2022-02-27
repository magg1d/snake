import pygame
pygame.init()

if True:
    WIDTH, HEIGHT = 600, 600

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")

    FPS = 10

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
    VELO = 0.5
    BORDER_COLOR = WHITE
    FILL_COLOR = GREEN

    def __init__(self):
        self.headx = WIDTH//2
        self.heady = HEIGHT//2
        self.xvel = self.VELO
        self.yvel = 0
        self.headwidth = SCALE
        self.headheight = SCALE

    def change_dir(self, dir):
        if dir == 0:
            self.xvel = 0
            self.yvel = -1 * self.VELO
            #self.heady += self.yvel
        elif dir == 1:
            self.xvel = self.VELO
            self.yvel = 0
            #self.headx += self.xvel
        elif dir == 2:
            self.xvel = 0
            self.yvel = self.VELO
            #self.heady += self.yvel
        elif dir == 3:
            self.xvel = -1*self.VELO
            self.yvel = 0
            #self.headx += self.xvel
        else:
            return

    def move(self):
        self.headx += self.xvel * SCALE
        self.heady += self.yvel * SCALE

    def draw(self, win):
        self.move()
        pygame.draw.rect(win, self.BORDER_COLOR, ((self.headx//SCALE) * SCALE, (self.heady//SCALE) * SCALE, self.headwidth, self.headheight))
        pygame.draw.rect(win, self.FILL_COLOR, (((self.headx//SCALE) * SCALE)+2, ((self.heady//SCALE) * SCALE)+2, self.headwidth-4, self.headheight-4))
        pygame.display.update()
        

def draw(win,snake):
    win.fill(BLACK)
    snake.draw(win)
    pygame.display.update()


def handle_snake_direction(keys, snake):
    if keys[pygame.K_UP] and snake.yvel == 0: #and left_paddle.y - left_paddle.VEL >= 0:
        snake.change_dir(0)
    if keys[pygame.K_RIGHT] and snake.xvel == 0: #and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        snake.change_dir(1)
    if keys[pygame.K_DOWN] and snake.yvel == 0: #and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        snake.change_dir(2)
    if keys[pygame.K_LEFT] and snake.xvel == 0: #and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        snake.change_dir(3)

def main():
    run = True
    clock = pygame.time.Clock()

    snake = Snake()

    while run:
        clock.tick(FPS)
        draw(WIN, snake)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        key = pygame.key.get_pressed()
        handle_snake_direction(key, snake)

    pygame.quit()

main()