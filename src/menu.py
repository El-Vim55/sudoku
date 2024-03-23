import pygame

f = 0xffffff
pygame.init()
surface = pygame.display.set_mode((550, 400))
surface.fill(0x344e5b)
pygame.display.set_caption("Main Menu")

font = pygame.font.SysFont('arial', 40)
easy = font.render("Easy", True, (255,255,255))
easyRec = text.get_rect()
easyRec.center = (273, 75)

# def draw_text(text, font, x, y):
#     img = font.render(text, True, 0xffffff)
#     screen.blit(img, (x,y))

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        surface.blit(text, rec)

    pygame.display.update()
