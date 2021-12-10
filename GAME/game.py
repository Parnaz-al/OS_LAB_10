import random
import arcade
from pyglet.window.key import S


SCREEN_WIDTH = 500
SCREEN_HEIGHT= 500
t=0
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.color=arcade.color.AMAZON
        self.body_size = 0
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2 
        self.speed = 4
        self.body=[]
        self.score = 0
        self.change_x = 0
        self.change_y = 0
    
      
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        for part in self.body:
            arcade.draw_rectangle_filled(part[0],part[1],self.width,self.height,self.color)
    def move(self):
        self.body.append([self.center_x,self.center_y])
        
        if len(self.body)> self.body_size:
            self.body.pop(0)
            
        
        if self.change_x ==-1:
            self.center_x -=self.speed
        elif self.change_x ==1:
            self.center_x +=self.speed
     
                
        if self.change_y ==-1:
            self.center_y -=self.speed
        elif self.change_y ==1:
            self.center_y +=self.speed
        
                
       
                
     
     
    def eat(self):
        self.body_size +=1
       
        
    
              
    
        


class Apple(arcade.Sprite):
    
   def __init__(self):
        super().__init__()
        arcade.Sprite.__init__(self)
        self.image = 'image1.png' 
        self.apple = arcade.Sprite(self.image, 0.3)
        self.width =16
        self.height=16    
        self.apple.center_x = random.randint(20,SCREEN_WIDTH-20)  
        self.apple.center_y = random.randint(20, SCREEN_HEIGHT-20)  

   def draw(self):
        self.apple.draw()



class Poop(arcade.Sprite):
    
   def __init__(self):
        arcade.Sprite.__init__(self)
        self.image = 'image2.png'  
        self.poop = arcade.Sprite(self.image, 0.1)  
        self.width =16
        self.height=16   
        self.poop.center_x = random.randint(20,SCREEN_WIDTH-20)  
        self.poop.center_y = random.randint(20, SCREEN_HEIGHT-20)  

   def draw(self):
        self.poop.draw()
        


class Pear(arcade.Sprite):
    
   def __init__(self):
        arcade.Sprite.__init__(self)
        self.image = 'image3.png'  
        self.pear = arcade.Sprite(self.image, 0.3)  
        self.width =16
        self.height=16   
        self.pear.center_x = random.randint(20,SCREEN_WIDTH-20)  
        self.pear.center_y = random.randint(20, SCREEN_HEIGHT-20)  

   def draw(self):
        self.pear.draw()
        
                
        
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=500,title='snake game')
        arcade.set_background_color(arcade.color.WHITE)
        self.snake =Snake()
        self.apple =Apple()
        self.poop=Poop()
        self.pear=Pear()
        
       

    def on_draw(self):
       arcade.start_render()
       self.snake.draw()
       self.apple.draw()
       self.poop.draw()
       self.pear.draw()
       arcade.draw_text(f"Score: {self.snake.score}",start_x= 10, start_y= 10 ,color=arcade.color.BURNT_ORANGE,font_size = 20)
       
       if self.snake.center_x <= 0 or self.snake.center_x >= SCREEN_WIDTH or self.snake.center_y <= 0 or self.snake.center_y >= SCREEN_HEIGHT  or self.snake.score < 0 :
            arcade.draw_text('GAME OVER', start_x= 40, start_y= 250,color= arcade.color.BLACK, font_size = 70)
            
            
      
    def update(self,delta_time:float):
       self.snake.move()
       if arcade.check_for_collision(self.apple.apple,self.snake):
           self.snake.eat()
           self.snake.score+=1
           self.apple=Apple()
           
       elif arcade.check_for_collision(self.pear.pear,self.snake):    
           self.snake.eat()
           self.pear=Pear()
           self.snake.score+=2
           
        
       elif arcade.check_for_collision(self.poop.poop,self.snake):    
           self.snake.eat()
           self.poop=Poop()
           self.snake.score-=1
           
      
      
 
    def on_key_release(self, key: int, modifiers: int):
      
     if key == arcade.key.LEFT:
        self.snake.change_x= -1
        self.snake.change_y= 0
     
     elif key ==arcade.key.UP:
         self.snake.change_y= 1 
         self.snake.change_x= 0
     elif key==arcade.key.DOWN:
         self.snake.change_y= -1
         self.snake.change_x= 0
     elif key==arcade.key.RIGHT:
         self.snake.change_x= 1 
         self.snake.change_y= 0     
        
my_game =Game()

arcade.run()

