import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ultimate Paintball')


#define player action variables
moving_left = False
moving_right = False


class Paintballer(pygame.sprite.Sprite):
  def __init__(self, x, y, scale, speed):
    pygame.sprite.Sprite.__init__(self)
    self.speed = speed

    img = pygame.image.load('img/player/Idle/0.png')
    self.image = pygame.transform.scale(img, (int(img.get_width() * scale, int(img.get_height() * scale)))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

  def draw(self, moving_left, moving_right):
    #reset movement variables

    #assign movement variables if moving left or right
    if moving_left:

    if moving_right:

  def draw(self)
  screen.blit(self.image, self.rect)

player = Paintballer(200, 200, 3, 5)

x = 200
y = 20 0
scale = 3


run = True
while run:


  player.draw()

  for event in pygame.event.get():
    #quit game
    if event.type == pygame.QUIT
       run = False
    #keyboard presses
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        moving_left = True
      if event.key == pygame.K_d:
        moving_right = True
      if event.key == pygame.K_ESCAPE:
        run == False

   #keyboard button released
   if event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        moving_left = False
      if event.key == pygame.K_d:
        moving_right = False

pygame.display.update()

pygame.quit()
