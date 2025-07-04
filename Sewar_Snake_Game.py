from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    #intiate Canvas 
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.clear()
    
    snake_x, snake_y ,snake_id = intiate_game(canvas)
    animate(canvas, snake_x, snake_y,snake_id)
    
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

def intiate_game(canvas):
    
 # Create the snake starting at top-left corner
    snake_x = 0
    snake_y = 0
    snake = [(snake_x, snake_y)]
    snake_id = draw_snake(canvas, snake_x, snake_y, "blue")

# add the food starting randomaly 
    food_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
    food_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
    food_id = draw_food(canvas,food_x,food_y,"red")
    
    return snake_x, snake_y , snake_id

def animate(canvas, snake_x, snake_y,snake_id):
    direction = 'right'  # Start moving to the right

    while True:  # animation loop
        time.sleep(DELAY)

        #  Move the snake in the current direction - move 20 pixels in the current direction

        snake_x += SIZE

        # Move snake to new position
        canvas.moveto(snake_id, snake_x, snake_y)
       

   
   

if __name__ == '__main__':
    main()
