""" 
1. create the pygame 9x9 box with the 9 boxes - DONE
2. initialize the starting numbers in the grid - DONE
3. create sudoku game logic - Ongoing
    - Create User interaction with keyboard or mouse interaction -
    - Allow user to edit open boxes and highlight selected boxes - <- XXXX


1. create 9x9 box sprites in pygame - DONE
   - test sprite by allowing highlight feature - DONE
2. initialize starting nums - DONE
3. Allow editing of these nums - DONE
4. Allow re-editing - DONE
5. Create Submit button and implement logic checker to check game - <-
"""

# Libraries
import pygame
import error_handling
import button
from random import randint

# Constants
WHITE = 0xFFFFFF
BLACK = 0x000000
GREY  = 0xeaeef4
DBLUE = 0x5a7bc0
LBLUE = 0xc3dafa

# Setup
pygame.init()
pygame.display.set_caption('Sudoku??? ¯\_(ツ)_/¯')
window_surface = pygame.display.set_mode((750,850))
window_surface.fill(WHITE)

# Button
submit_img_unclicked = pygame.image.load('img/submit-bttn.png').convert_alpha()
submit_img_clicked = pygame.image.load('img/submit-bttn-click.png').convert_alpha()
submit_bttn = button.Button(766, 566, submit_img_clicked, submit_img_unclicked, 1)

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

def difficulty():
    pass

def create_random_nums() -> list[list]:
    pass


class SudokuGrid(pygame.sprite.Sprite):
    def __init__(self, value, row, col, sizeX, sizeY, font):
        super().__init__()
        self.value = value
        self.row   = row
        self.col   = col
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.font  = font
        self.selected = False
        self.editing  = False
        self.initial  = False
        self.image = pygame.Surface((80, 80))
        self.rect  = self.image.get_rect(topleft=(col*80, row*80))


    def set_initial(self):
        self.initial = True

    def is_initial(self):
        return self.initial

    def update(self):
        submit_bttn.operation(self.image)
        if self.selected:
            highlight_rect = pygame.Rect(((self.sizeX // 9)-5, (self.sizeY // 9)-5), (74,74))
            self.image.fill(LBLUE, highlight_rect) 
        else:
            self.image.fill(WHITE)

        i = 1
        while (i*80) < 720:
            if (i*80) % 3 == 0:
                pygame.draw.rect(self.image, BLACK, self.image.get_rect(), 3)
            else:
                pygame.draw.rect(self.image, BLACK, self.image.get_rect(), 1)
            i+=1

        if self.value != 0:
            text_color = BLACK if self.is_initial() else DBLUE
            text = self.font.render(str(self.value), True, text_color)
            highlight_rect = pygame.Rect(((self.sizeX // 9)-5, (self.sizeY // 9)-5), (74,74))
            if not self.is_initial():
                self.image.fill(GREY, highlight_rect)
            else:
                self.image.fill(WHITE, highlight_rect)
            self.image.blit(text, ((self.sizeX // 3) -1, (self.sizeY // 3) -7))


def create_grid_sprite() -> pygame.sprite:
    sprites = pygame.sprite.Group()
    for i in range(9):
        for j in range(9):
            cell = SudokuGrid(initial_nums[i][j], i, j, 80, 80, font)
            if initial_nums[i][j] != 0:
                cell.set_initial()
            sprites.add(cell)
    return sprites

def get_clicked_cell(mouse_x, mouse_y) -> (int, int):
    row = mouse_y // (720 // 9)
    col = mouse_x // (720 // 9)
    print(row, col)
    return row, col


if __name__ == '__main__':
    font = pygame.font.SysFont(None, 80)
    grid_sprite = create_grid_sprite()

    clock = pygame.time.Clock()


    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_row, selected_col = get_clicked_cell(mouse_x, mouse_y)

                # Update cell selection and editing
                for cell in grid_sprite:
                    cell.selected = (cell.row == selected_row and cell.col == selected_col)
                    cell.editing = (cell.selected and cell.value == 0) or (cell.selected and not cell.is_initial())

            elif event.type == pygame.KEYDOWN:
                if any(cell.editing for cell in grid_sprite):
                    key = event.unicode
                    # Update cell value in editing mode
                    if key.isdigit() and 1 <= int(key) <= 9:
                        for cell in grid_sprite:
                            if cell.editing:
                                cell.value = int(key)
                                cell.editing = True

        # Refresh the screen
        submit_bttn.operation(window_surface)
        grid_sprite.update()
        sprites_to_blit = [(sprite.image, sprite.rect) for sprite in grid_sprite]
        window_surface.blits(sprites_to_blit)
        pygame.display.flip()
        
    
        # drivers
        # create_grid_sprite()
        # create_grid()
        # initialize_nums(initial_nums)
        # user_interaction(initial_nums)

        # display
        # pygame.display.update()
    # pygame.draw.rect(window_surface, BLACK, pygame.Rect(15, 15, 720, 720), 3)
    # i = 1
    # while(i*80) < 720:
    #     if (i * 80) % 3 == 0:
            # pygame.draw.line(window_surface, BLACK, pygame.Vector2((i * 80) + 15, 15), pygame.Vector2((i * 80) + 15, 734), 3)
    #         pygame.draw.line(window_surface, BLACK, pygame.Vector2(15, (i * 80) + 15), pygame.Vector2(734, (i * 80) +15), 3)
    #     else:
    #         pygame.draw.line(window_surface, BLACK, pygame.Vector2((i * 80) + 15, 15), pygame.Vector2((i * 80) + 15, 734), 1)
    #         pygame.draw.line(window_surface, BLACK, pygame.Vector2(15, (i * 80) + 15), pygame.Vector2(734, (i * 80) +15), 1)
    #     i+=1