import pygame

# pygame.init()
# windows_surface = pygame.display.set_mode((750, 750))
# windows_surface.fill(0xFFFFFF)
# is_running = True

class Button():
    def __init__(self, x, y, image_clicked, image_unclicked, scale):
        width = image_unclicked.get_width()
        height = image_unclicked.get_height()
        scaled_size = int(width*scale), int(height*scale)
        self.image_clicked = pygame.transform.scale(image_clicked, scaled_size)
        self.image_unclicked = pygame.transform.scale(image_unclicked, scaled_size)
        self.image = image_unclicked
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def operation(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                print("clicked")
                self.image = self.image_clicked
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.image = self.image_unclicked
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

# submit_img_unclicked = pygame.image.load('img/submit-bttn.png').convert_alpha()
# submit_img_clicked = pygame.image.load('img/submit-bttn-click.png').convert_alpha()
# submit_bttn = Button(344, 344, submit_img_clicked, submit_img_unclicked, 1)

# while is_running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False
#     # submit_bttn.draw_button()
#     submit_bttn.operation(windows_surface)
#     pygame.display.update()
