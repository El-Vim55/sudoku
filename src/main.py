""" 
1. create the pygame 9x9 box with the 9 boxes - DONE
2. initialize the starting numbers in the grid - DONE
3. create sudoku game logic - Ongoing
    - Create User interaction with keyboard or mouse interaction -
    - Allow user to edit open boxes and highlight selected boxes - <-
"""

# Libraries
import pygame
import error_handling
from random import randint

# Constants
WHITE = 0xFFFFFF
BLACK = 0x000000
LBLUE = 0x325aaf

# Setup
pygame.init()
pygame.display.set_caption('Sudoku??? ¯\_(ツ)_/¯')
window_surface = pygame.display.set_mode((750,850))
window_surface.fill(WHITE)
font = pygame.font.SysFont(None, 80)

is_running = True

initial_nums = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]


class SudokuGrid(pygame.sprite.Sprite):
    def __init__(self, value, row, col, sizeX, sizeY):
        super().__init__()
        self.value = value
        self.row = row
        self.col = col
        self.sizeX = sizeX
        self.sizeY = sizeY
        # self.highlight = pygame.draw.rect(window_surface, LBLUE, size, size)
        self.edited = False
        self.selected = False
        

    def update(self):
        if self.selected:
            pass
            



def difficulty():
    pass

def create_random_nums() -> list[list]:
    pass


def create_grid() -> pygame.sprite:
    sprites = pygame.sprite.Group()
    pygame.draw.rect(window_surface, BLACK, pygame.Rect(15, 15, 720, 720), 3)
    
    i = 1
    while(i*80) < 720:
        if (i * 80) % 3 == 0:
            cell = pygame.draw.line(window_surface, BLACK, pygame.Vector2((i * 80) + 15, 15), pygame.Vector2((i * 80) + 15, 734), 3)
            cell = pygame.draw.line(window_surface, BLACK, pygame.Vector2(15, (i * 80) + 15), pygame.Vector2(734, (i * 80) +15), 3)
        else:
            cell = pygame.draw.line(window_surface, BLACK, pygame.Vector2((i * 80) + 15, 15), pygame.Vector2((i * 80) + 15, 734), 1)
            cell = pygame.draw.line(window_surface, BLACK, pygame.Vector2(15, (i * 80) + 15), pygame.Vector2(734, (i * 80) +15), 1)
        sprites.add(cell)
        i+=1

def initialize_nums(nums):
    for row in range(9):
        for col in range(9):
            output = nums[row][col]
            num_text = font.render(str(output), True, BLACK)
            window_surface.blit(num_text, pygame.Vector2((row * 80) + 40, (col * 80) + 30))

def create_game_logic(nums):
    for row in range(9):
        for col in range(9):
            if nums[col][row] != 45:
                pass

# create_game_logic(initial_nums)


# def check_board_logic():
#     for i in range(9):
#         for j in range(9):
#             pass

def user_interaction(grid):
    create_grid()

    highlight = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = x//16
                y = y//16
                
                # pygame.draw.rect(window_surface, LBLUE, (x*16, y*16, 32, 32), 5)
                # highlight = Trueb
                


        if highlight:
            pass
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key in range(pygame.K_1, pygame.K_9 + 1):
        #         number = event.key - pygame.K_0


        pygame.display.update()
        # else:
            # clicked = False

        # if event.type == pygame.KEYDOWN:
        #     pass
        # if event.type == pygame.KEYUP:
        #     moveY -= 1
        # if event.type == pygame.K_LEFT:
        #     moveX -= 1
        # if event.type == pygame.K_RIGHT:
        #     moveX += 1


if __name__ == '__main__':
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        
        # drivers
        # create_grid()
        initialize_nums(initial_nums)
        user_interaction(initial_nums)

        # display
        pygame.display.update()
