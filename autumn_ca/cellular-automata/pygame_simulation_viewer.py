import sys, pygame
from pygame.locals import *

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def simulation_viewer(simulation, screen_size, target_fps):
    
    # set up pygame
    pygame.init()
    clock = pygame.time.Clock()
    
    # set up the window
    windowSurface = pygame.display.set_mode(screen_size)#, pygame.FULLSCREEN | pygame.HWSURFACE)
    pygame.display.set_caption('Pygame CA Viewer')
    
    
    def create_surf_from_space(space):
    
        surf = pygame.Surface((space.shape[0], space.shape[1]))
        
        surf.fill(BLACK)
        
        for x,row in enumerate(space):
            for y,val in enumerate(row):
            
                if( val == 1 ):
                    surf.fill(RED, ((x,y),(1,1)))

        return pygame.transform.scale(surf, screen_size)     
        
    # run the game loop
    while True:
        
        current_space = next(simulation)
        
        surf = create_surf_from_space (current_space)
        
        windowSurface.blit(surf,windowSurface.get_rect())
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                
                    pygame.quit()
                    
                    raise StopIteration
                
        yield 
                
        clock.tick(target_fps)
        
        

        