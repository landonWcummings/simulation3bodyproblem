import pygame
from backend.model import Game

class model:
  def __init__(self, window, width, height):
    self.game = Game(window,width, height)
    
  
  def play(self):
    width, height = 1000, 700
    window = pygame.display.set_mode((width, height))
    setstart = [[width /2 + 35,height/2 + 12,-0.4,-0.5],[width /2-25,height/2-13,-0.3,0.5],[width /2 + 5,height/2 -12,-0.2,0.1]]
    game = Game(window,width,height)

    run = True
    clock = pygame.time.Clock()
    while run:
      clock.tick(150)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
          break
      
      keys = pygame.key.get_pressed()
      if keys[pygame.K_SPACE]:
        game.reset()
      
      game.loop()
      
      game.draw()
      pygame.display.update()
    
  pygame.quit()

width, height = 700, 500
window = pygame.display.set_mode((width, height))

m = model(window,width,height)
m.play()