#import required libraries
import pygame
import random
import sys

#initialize variables
#number of inital particles
num_particles = 500
max_speed = 3
min_speed = -3
Particle_size = 10
#Background color
BG = (0, 0, 0)
# Create particle class using pygame sprites
class Particle(pygame.sprite.Sprite):
    # initialize size, location, speed & color
    def __init__(self, width, height, px, py, sx, sy, color):
        super().__init__()
        #size
        self.image = pygame.Surface([width, height])
        # color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #position
        self.rect.center = [px, py]
        #Speed
        self.sx = sx
        self.sy = sy
    
    
    def update(self):
       
       # move particles
        self.rect.move_ip(self.sx, self.sy)
       # enforce screen boundaries
        if self.rect.right >= Display.current_w or self.rect.left <= 0:
           self.sx *= -1
        if self.rect.bottom >= Display.current_h or self.rect.top <= 0:   
            self.sy *= -1
        # allow particles to interact
        #if pygame.sprite.spritecollide(self, particle_tracker, 0):
         #   col_list = pygame.sprite.spritecollide(self, particle_tracker, False)
          #  for col in col_list:
           #     if self.rect.top - col.rect.bottom == 0:
            #        self.sy = sum(col.sy,self.sy)/2
             #       self.sx = sum(col.sx, self.sx)/2
              #      col.sy = self.sy
               #     col.sx = self.sx
                #    self.rect.centerx = col.rect.centerx + Particle_size
                 #   self.rect.centery = col.rect.centerx + Particle_size

            
                
# initiate pygame
pygame.init()
# track user monitor in variable
Display = pygame.display.Info()
# set game screen to match the size of Display
screen = pygame.display.set_mode((Display.current_w,Display.current_h))
print(screen)
# Rename game window
pygame.display.set_caption('Struct Emerge')

# create time variable 
clock = pygame.time.Clock()
# generate new particles into particle group 
particle_tracker = pygame.sprite.Group()
for particle in range(num_particles):
    new_particle = Particle(Particle_size, Particle_size, random.randrange(Particle_size, Display.current_w - Particle_size), random.randrange(Particle_size, Display.current_h - Particle_size),random.randint(min_speed,max_speed),random.randint(min_speed,max_speed), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    particle_tracker.add(new_particle)
    

# run game loop
while True:
    # use events
    for event in pygame.event.get():
        # End sim instance when user closes window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update the full display surface
    screen.fill(BG)
    particle_tracker.update()
    particle_tracker.draw(screen)
    pygame.display.flip()
    # limit maximum framerate to 60 FPS
    clock.tick(60)