import pygame

class LR_Endzone(pygame.sprite.Sprite):
    '''This class defines the sprite for the left and right end zones'''
    def __init__(self,screen,x_position):
        '''This initializer takes a screen surface, and x position as
        parameters'''
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #10 pixel wide endzones
        self.image = pygame.Surface((50,screen.get_height()))
        self.image = self.image.convert()
        self.image.fill ((204,204,204))
        
        #Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = x_position
        self.rect.top = 0
        
class Top_Endzone(pygame.sprite.Sprite):
    '''This class defines the sprite for the top endzones'''
    def __init__(self,screen,colour,y_position):
        '''This initializer takes  ascreen surface'''
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #10 pixel height endzone
        self.image = pygame.Surface(((screen.get_width()-50),40))
        self.image = self.image.convert()
        self.image.fill (colour)
        
        #Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = 50
        self.rect.top = y_position
        
class Ball(pygame.sprite.Sprite):
	"""A ball that will move across the screen
	Returns: ball object
	Functions: update, calcnewpos
	Attributes: area, vector"""

	def __init__(self,screen, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image= self.rect = pygame.image.load('ball.png')
		self.area = screen.get_rect()
		self.vector = vector

	def update(self):
		newpos = self.calcnewpos(self.rect,self.vector)
		self.rect = newpos

	def calcnewpos(self,rect,vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)
            
             
class Brick(pygame.sprite.Sprite):
    '''This class defines the sprite for the bricks'''
    def __init__(self,screen,x_position,y_position,colour):
        '''This initializer takes a screen surface, different x-positions,
        and y-positions, along with the colour of the bricks'''
        #Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #Set position and colour variables
        self.__x_position = x_position
        self.__y_position = y_position
        self.__colour = colour
        
        #Create attributes for each brick
        self.image = pygame.Surface((30,15))
        self.image.fill(self.__colour)
        
        self.rect = self.image.get_rect()
        
        self.rect.left = self.__x_position
        self.rect.top = self.__y_position
        
        
class Player(pygame.sprite.Sprite):
    '''This class defines the sprite for the players paddle'''
    def __init__(self,screen,player_num):
        '''This initializer takes a screen surface, initializes the image
        and rect attributes, and sets a y direction that the player moves'''
        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        #Set the image and rect attributes for the players paddle
        self.image = pygame.Surface((90,10))
        self.image = self.image.convert()
        self.image.fill ((255,0,0))
        self.rect = self.image.get_rect()
        
        #Initialize player 1
        if player_num == 1:
            self.rect.bottom = screen.get_height()
        else:
            self.rect.bottom = screen.get_height() - 20
            
        self.rect.centerx = screen.get_width()/2
        self.__screen = screen
        
        #Set the initial X direction of the player
        self.__dx = 0
        
    def change_direction(self, xy_change):
        '''This method takes a (x,y) tuple as a parameter, extraxts the x
        element from it, and uses it to set the players x direction and
        increases the speed by 5'''
        self.__dx = xy_change[0]
        
    def resize(self):
        self.image = pygame.transform.scale(self.image,(45,10),)
        
    def update(self):
        '''This method wil be called automatically to reposition the player
        sprite on the screen.'''
        #Check to see if we hit the left or right endzone
        if ((self.rect.left > 50) and (self.__dx > 0)) or\
           ((self.rect.right < self.__screen.get_width()-50) and (self.__dx < 0)):
            self.rect.right -= (self.__dx*5)
            
class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines a label sprite to display the score.'''
    def __init__(self):
        '''This initializer loads the system font "Arial", and
        sets the starting score to 0'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
 
        # Load our custom font, and initialize the starting score.
        self.__font = pygame.font.SysFont("Arial", 30)
        self.__score =0
    
    def score(self,score):
        '''This method takes in the number of bricks missing and subtracts the
        total amount to the amount on the screen'''
        self.__score = 108 - score
    
        
    def update(self):
        '''This method will be called automatically to display 
        the current score at the top of the game window.'''
        message = "Score:%d" % (self.__score)
        self.image = self.__font.render(message, 1, (0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (320, 10)
        

    