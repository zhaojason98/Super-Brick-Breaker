#Import and Initialize
import pygame, BreackerSprites
pygame.init()
screen = pygame.display.set_mode((640,480))

def main():
    '''This function defines the 'mainline logic' for our Super Brick
    Breacker Game'''
    
    #Display
    pygame.display.set_caption("Super Brick Breacker")
    
    #Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))
    screen.blit(background,(0,0))
    
    #Sprites for: End Zones, Bricks, Player, and Ball
    score_keeper = BreackerSprites.ScoreKeeper()
    ball = BreackerSprites.Ball(screen,5)
    player1 = BreackerSprites.Player(screen,1)
    player2 = BreackerSprites.Player(screen,2)
    left_endzone = BreackerSprites.LR_Endzone(screen,0)
    right_endzone = BreackerSprites.LR_Endzone(screen,590)
    top_endzone = BreackerSprites.Top_Endzone(screen,(204,204,204),0)
    bottom_endzone = BreackerSprites.Top_Endzone(screen,(0,0,0),screen.get_height()-1)
    #Bricks
    bricks = []
    colour = (0,0,255)
    top = 80
    #6 Rows
    for row in range (6):
        #18 columns
        for column in range (0,18):
            #Set colours for each row
            if row == 1:
                colour = (0,255,0)
            elif row == 2:
                colour = (255,102,0)
            elif row == 3:
                colour = (255,255,0)
            elif row == 4:
                colour = (255,0,0)
            elif row == 5:
                colour = (255,255,255)
            #Create each brick with a x and colour    
            brick = BreackerSprites.Brick(screen,column * 30 + 50,top,colour)
            bricks.append(brick)
        #Puts the next row pixels up
        top += 16
    
    #Group
    allSprites = pygame.sprite.OrderedUpdates(top_endzone,score_keeper,player1,player2,ball,left_endzone,right_endzone,bricks)
    Out_Group = pygame.sprite.Group(bottom_endzone)
    ball_group = pygame.sprite.Group(ball)
    brick_group = pygame.sprite.Group(bricks)
    
    #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    lives = 3
    
    pygame.mouse.set_visible(False)
    
    #Loop
    while keepGoing:
        
        #Time
        clock.tick(30)
        
        #Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.change_direction((1,0))
                if event.key == pygame.K_RIGHT:
                    player1.change_direction((-1,0))
            elif event.type == pygame.JOYHATMOTION:
                player2.change_direction(event.value)
                
        #Checks to see if player hits the ball
        #Cuts the size in half when half the bricks are gone
        if len(brick_group) < 54:
            player1.resize()
            player2.resize()
        #Exits when lives run out or all bricks are gone
        if lives < 0 or len(brick_group) == 0:
            keepGoing = False
                
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
        
    pygame.quit()
    
main()
                
    