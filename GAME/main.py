import random
import arcade

SCREENWIDTH = 500
SCREENHEIGHT = 500

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREENWIDTH ,height=SCREENHEIGHT,title="SNAKE game")
        arcade.set_background_color(arcade.color.BRIGHT_GREEN)
        self.snake = Snake()
        self.food = Food()
        self.poop =

    def on_draw(self):
        arcade.start_render() 
        self.snake.draw()
        self.food.draw()
        s

    def on_key_release(self, character: int, modifiers: int):
        if character == arcade.key.LEFT :
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif character == arcade.key.RIGHT :
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif character == arcade.key.UP : 
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif character == arcade.key.DOWN :
            self.snake.change_y = -1
            self.snake.change_x = 0

    def on_update(self, delta_time: float):
        self.snake.move() 

        if arcade.check_for_collision(self.snake,self.food) :
            self.snake.eat()
            self.food = Food()  
            print(self.snake.score)     
    
class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 16
        self.height = 16
        self.score = 0
        self.color = arcade.color.BLUE
        self.change_x = 0
        self.change_y = 0
        self.body_size = 0
        self.center_x = SCREENWIDTH //2
        self.center_y = SCREENHEIGHT//2
        self.speed = 4
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

        for i in range(len(self.body)):
            arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width,self.height,self.color)

    def eat(self):
        self.score +=1

    def move(self):
        self.body.append([self.center_x,self.center_y])

        if len(self.body) > self.score :
            self.body.pop(0)

        if self.change_x > 0 :
            self.center_x += self.speed
        elif self.change_x < 0 :
            self.center_x -= self.speed

        if self.change_y > 0 :
            self.center_y += self.speed
        elif self.change_y < 0 :
            self.center_y -= self.speed    
    
        
class Food(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.image = 'image1.png' 
        self.fOod = arcade.Sprite(self.image, 0.1) 
        self.width = 16
        self.height = 16
        self.fOod.center_x = random.randint(0,SCREENWIDTH)
        self.fOod.center_y = random.randint(0,SCREENHEIGHT)

    def draw(self):
        self.fOod.draw()

class NegtivePoint(arcade.Sprite) :
    def __init__(self) :
        super().__init__()

        self.image = 'image1.png'  
        self.NP = arcade.Sprite(self.image, 0.1)  
        self.width =16
        self.height=16   
        self.fOod.center_x = random.randint(0,SCREENWIDTH)
        self.fOod.center_y = random.randint(0,SCREENHEIGHT)
    def draw(self):
        self.NP.draw()

my_game=Game()
arcade.run()