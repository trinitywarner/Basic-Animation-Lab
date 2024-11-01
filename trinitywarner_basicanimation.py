""" IDEA / ALTER """
""" Make a Box """

def main():
    #i: import & intililize
    import pygame
    pygame.init()
    
    #d: displays configuration
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Man, I'm hungry...")
    
    #e: entities
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load('C:/Users/warne/OneDrive/Desktop/CS 120 Labs/background2.png')
    screen.blit(background, (0, 0))
    
    #make a meal box 25 x 25
    #box = pygame.Surface((25, 25))
    box = pygame.image.load('C:/Users/warne/OneDrive/Desktop/CS 120 Labs/burger#7.png')
    box = box.convert_alpha()
    #box = pygame.trandform.scale(box, (100, 100))
    #box.fill((0, 0, 0))

    #setting up the box variables
    box_x = 0
    box_y = 200

    #action alter begins below
    #a: action (alter begins below)
    
        #a: assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    
        #l: main loop set-up
    while keepGoing:
        
        #t: timer to set frame rate
        clock.tick(30)
        
        #e
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify box value
        box_x += 5
        if box_x > screen.get_width():
            box_x = 0

        #r
        screen.blit(background, (0,0))
        screen.blit(box, (box_x, box_y))
        pygame.display.flip()
                
    pygame.quit()
    
if __name__ == "__main__":
    main()