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
   (15%) - Logic checker will be created by checking each column and rows and each 3x3 grid, also check for duplicates
"""

# Libraries
import pygame
import message_handling as mh
import button
import threading
from random import randint

# Colours
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
submit_bttn = button.Button(525, 750, submit_img_clicked, submit_img_unclicked, 1)

is_running = True

# initial_nums = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#         ]
    
initial_nums=[
[7, 5, 1,  8, 8, 3,  9, 2, 6],
[8, 9, 3,  6, 2, 5,  1, 7, 4], 
[6, 4, 2,  1, 7, 9,  5, 8, 3],
[4, 2, 5,  3, 1, 6,  7, 9, 8],
[1, 7, 6,  9, 8, 2,  3, 4, 5],
[9, 3, 8,  7, 5, 4,  6, 1, 2],
[3, 6, 4,  2, 9, 7,  8, 5, 1],
[2, 8, 9,  5, 3, 1,  4, 6, 7],
[5, 1, 7,  4, 6, 8,  2, 3, 9]]

def difficulty():
    pass

def create_random_grid() -> list[list]:  # based on difficulty
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

        submit_bttn.operation(window_surface)
        # if submit_bttn.operation(window_surface):
        #     logic_checker(initial_nums)

def create_grid_sprite() -> pygame.sprite:
    sprites = pygame.sprite.Group()
    for i in range(9):
        for j in range(9):
            cell = SudokuGrid(initial_nums[i][j], i, j, 80, 80, font)
            if initial_nums[i][j] != 0:
                cell.set_initial()
            sprites.add(cell)
    return sprites

run_logic_checker = False
run_thread = False

def logic_checker(grid):
    # 9x9
    errors = 0
    for row in range(9):
        row_values = grid[row]
        dup_val = set(row_values)
        if len(dup_val) < 9: 
            mh.duplicate_value()
            errors = 1
        elif sum(row_values) != 45:
            print('wrong')
            errors = 1

        res = []
        column = []
        for col in range(9):
            column.append(grid[col][row])
        res.append(column)

    for column_values in res:
        dup_val = set(column_values)
        if len(dup_val) < 9:
            print("Duplicate!")
            errors = 1
        elif sum(column_values) != 45:
            print('not equal')
            errors = 1

    # 3x3
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subGrid = grid[row][col:col+3] + grid[row+1][col:col+3] + grid[row+2][col:col+3]
            dup_val = set(subGrid)
            if len(dup_val) < 9:
                print("dup")
                errors = 1
            elif sum(subGrid) != 45:
                print('wrong')
                errors = 1
    
    if errors == 0:
        print('you win')


def run_logic_checker_thread():
    global run_logic_checker
    while True:
        if run_logic_checker:
            logic_checker(initial_nums)
            run_logic_checker = False

logic_checker_thread = threading.Thread(target=run_logic_checker_thread, daemon=True)
logic_checker_thread.start()

def get_clicked_cell(mouse_x, mouse_y) -> (int, int):
    row = mouse_y // (720 // 9)
    col = mouse_x // (720 // 9)
    print(row, col)
    # print(row, col)
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
                if submit_bttn.operation(window_surface):
                    run_logic_checker = True

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
                                initial_nums[cell.row][cell.col] = cell.value
                                cell.editing = True

        # Refresh the screen
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