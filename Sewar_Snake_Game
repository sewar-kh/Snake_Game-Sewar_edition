from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

def main():
    intiate_game()

def draw_square(canvas,x,y,color):
    size = SIZE
    left_x = x
    top_y = y
    right_x = left_x + size
    bottom_y = top_y + SIZE
    rect_id = canvas.create_rectangle(
        left_x, 
        top_y, 
        right_x, 
        bottom_y,
        color
    )
    return rect_id
     
def draw_snake(canvas,x,y,color):
    return draw_square(canvas,x,y,color)
    
def draw_food(canvas,x,y,color):
    return draw_square(canvas,x,y,color)

def intiate_game():

 #intiate Canvas 
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.clear()

   # add the food starting randomaly 
    food_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
    food_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
    food_id = draw_food(canvas,food_x,food_y,"red")
    
 # Create the snake starting at top-left corner
    snake_x = 0
    snake_y = 0
    snake = [(snake_x, snake_y)]
    snake_ids = [draw_snake(canvas, snake_x, snake_y, "blue")]

if __name__ == '__main__':
    main()
