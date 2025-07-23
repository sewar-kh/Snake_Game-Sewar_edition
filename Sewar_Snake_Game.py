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

    """ #before milestone 5 : 

    snake_x, snake_y ,snake_id = intiate_game(canvas)
    
    #milestone 5 : 
    snake_x, snake_y , snake_id , food_x , food_y , food_id = intiate_game(canvas) 
    
    #milestone 6 - growing snake  : 
    #change  snake_id to  snake_ids
    snake, snake_x, snake_y , snake_ids , food_x , food_y , food_id = intiate_game(canvas) 
    
    # milestone 8 : adding scoring 
    snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id = intiate_game(canvas)
    """
    """ #before milestone 5 : 
    animate(canvas, snake_x, snake_y,snake_id)
    
    # milestone 5 : 
    animate(canvas, snake_x, snake_y,snake_id, food_x, food_y, food_id)
    
    # milestone 6 : 
    #change  snake_id to  snake_ids
    animate(canvas, snake, snake_x, snake_y,snake_ids, food_x, food_y, food_id)
    
    # milestone 8 : adding scoring 
    animate(canvas, snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id)
    """
     # milestone 9 :  Pass delay into animate()
    snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id, delay = intiate_game(canvas)
    animate(canvas, snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id, delay)


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
    delay = show_start_screen(canvas) # MILESTONE 9: show start screen and get delay
    
 # Create the snake starting at top-left corner
    snake_x = 0
    snake_y = 0
    snake = [(snake_x, snake_y)]

    """#before milestone 6 - growing snake : 
    snake_id = draw_snake(canvas, snake_x, snake_y, "blue")
    """
    #milestone 6 : growing snake
    #change  snake_id to  snake_ids
    snake_ids = [draw_snake(canvas, snake_x, snake_y, "blue")]

    # add the food starting randomaly 
    food_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
    food_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
    food_id = draw_food(canvas,food_x,food_y,"red")

    """ #before milestone 5 :
    return snake_x, snake_y , snake_id
    
    #milestone 5 : 

    return  snake_x, snake_y , snake_id , food_x , food_y , food_id
    
    #milestone 6 : 
    #change  snake_id to  snake_ids
    return snake, snake_x, snake_y , snake_ids , food_x , food_y , food_id 
    """
    
    #milestone 8 - keeping scores : 
    
    score_count = 0
    score_text_id = canvas.create_text(
        10, 10, anchor='nw', 
        text="Score: 0", # another way : text=f"Score: {score_count}",
        font="Arial", font_size=14, color="black"
    )
    #return snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id
    
    # Milestone 9 - adding delay 
    """ returning delay so we can use the delay selected from the start screen
    inside the animate function."""
    return snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id, delay


# function for milestone # 2 and 3  

""" #before milestone 5 : 
def animate(canvas, snake_x, snake_y,snake_id):

# milestone 5 : 
def animate(canvas, snake_x, snake_y, snake_id, food_x, food_y, food_id):

# milestone 6 : 
#change  snake_id to  snake_ids

def animate(canvas, snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id):  

#milestone 8 - keeping scores :
def animate(canvas, snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id,score_count, score_text_id):  
"""
#milestone 9 : Update animate() to accept delay
def animate(canvas, snake, snake_x, snake_y, snake_ids, food_x, food_y, food_id, score_count, score_text_id, delay):

    direction = 'right'  # Start moving to the right
    just_ate = False

    while True:  # animation loop
        time.sleep(DELAY)

        #  Move the snake in the current direction - move 20 pixels in the current direction

        """ # milestone 2 - move only to the right 

        snake_x += SIZE
        """
        # Move snake to new position
        """
        canvas.moveto(snake_id, snake_x, snake_y)
        """
        #instead of using the previous to move only to the right - Move the snake in the current direction
        direction, snake_x, snake_y = change_position(canvas, direction, snake_x, snake_y)

        """
        # milestone 3 : Move snake to new position
        canvas.moveto(snake_id, snake_x, snake_y)
        """
        # milestone 6 : Move snake to new position
        """
        `moveto` function expects a single object ID (likely a string), but it is receiving a list when changing snake_id to 'snake_ids' on milestone 5, 
        which is a list of object IDs. One way to fix this : we can ensure that each ID in the `snake_ids` list is moved individually using the `moveto` function. I chose to use another method 
        """
        # milestone 6 : Compute new head position
        new_head = (snake_x, snake_y)
        snake.append(new_head)

        #milestone 6 : Draw new head
        new_head_id = draw_snake(canvas, snake_x, snake_y, "blue")
        snake_ids.append(new_head_id)

        # Remove tail if no food was eaten
        if not just_ate:
            old_x, old_y = snake.pop(0)
            old_id = snake_ids.pop(0)
            canvas.delete(old_id)
            
            """ # another way to write it :
            old_tail_id = snake_ids.pop(0)
            canvas.delete(old_tail_id)
            """

        #  Check for out of bounds
        """
        # milestone 4
        if out_of_bounds(canvas, snake_id):
            break
        
        # milestone 5 
        if out_of_bounds(canvas, snake_id): # : no change from milestone 4
            break
        food_x, food_y, food_id , just_ate = food_eaten(canvas,snake_x, snake_y,food_x,food_y,food_id)

        # milestone 6
        if out_of_bounds(canvas,snake_ids,food_id):  #adding food_id , change snake_id to snake_ids 
            break
        # no change from milestone 5 
        food_x, food_y, food_id , just_ate = food_eaten(canvas,snake_x, snake_y,food_x,food_y,food_id)

        # milestone 7 : no change from milestone 5 
        food_x, food_y, food_id , just_ate = food_eaten(canvas,snake_x, snake_y,food_x,food_y,food_id)

        # milestone 7 : implementing the animated Game Over screen + Play Again button
        if out_of_bounds(canvas, snake_ids[-1]):
            show_animated_game_over(canvas)
                       
            break
        """
        # milestone 8 : adding score_count 
        food_x, food_y, food_id , score_count, just_ate = food_eaten(canvas,snake_x, snake_y,food_x,food_y,food_id,score_count)

        # milestone 8 : canvas.change_text &  adding score_count to Check for out of bounds
        canvas.change_text(score_text_id, "Score: " + str(score_count))
        
        # milestone 8 : adding score_count 
        if out_of_bounds(canvas, snake_ids , score_count):
            show_animated_game_over(canvas, score_count) 
            break  # This line ensures the loop exits after showing the Game Over screen
    

     
# function for milestone # 3 
def change_position(canvas, direction, snake_x, snake_y):
    
    #  Handle key press and update direction

    key = canvas.get_last_key_press()
    if key == "ArrowLeft" and direction != "right":
            direction = "left"
    elif key == "ArrowRight" and direction != "left":
        direction = "right"
    elif key == "ArrowUp" and direction != "down":
        direction = "up"
    elif key == "ArrowDown" and direction != "up":
        direction = "down"
    
    #  Move the snake in the current direction

    if direction == 'right':
        snake_x += SIZE
    elif direction == 'left':
        snake_x -= SIZE
    elif direction == 'up':
        snake_y -= SIZE
    elif direction == 'down':
        snake_y += SIZE
    return direction, snake_x, snake_y

# function for Milestone #4: Detecting Collisions (Game Over)
""" # Milestone #4
def out_of_bounds(canvas,snake_id):

    x = canvas.get_left_x(snake_id)
    y = canvas.get_top_y(snake_id)

# milestone 6 :
def out_of_bounds(canvas,snake_ids,food_id):
    
    x = canvas.get_left_x(snake_ids[-1])
    y = canvas.get_top_y(snake_ids[-1])

    if x<0 or x >= CANVAS_WIDTH or y<0 or y >= CANVAS_HEIGHT :

        print("Game's over ! ")
        return True

    return False

# milestone 7 :
def out_of_bounds(canvas, snake_head_id):
    # No need for food_id here. so I removed it 
"""
# milestone 8 :
# adding score_count
def out_of_bounds(canvas,snake_ids,score_count):
    snake_head_id = snake_ids[-1]  #  get the last piece of the snake
    
    # milestone 7 : 
    x = canvas.get_left_x(snake_head_id)
    y = canvas.get_top_y(snake_head_id)

    # milestone 7 : Check that x and y are not None:
    if x is None or y is None:
        print("Warning: invalid snake head position.")
        return True  # treat as game over
    # milestone 7 : 
    return x<0 or x >= CANVAS_WIDTH or y<0 or y >= CANVAS_HEIGHT 

# Milestone #5: Moving the food and creating new food
#def food_eaten(canvas,snake_x, snake_y,food_x,food_y,food_id):

# milestone 8 : adding score_count
def food_eaten(canvas,snake_x, snake_y,food_x,food_y,food_id,score_count):
    if snake_x == food_x and snake_y == food_y:
        canvas.delete(food_id)

        score_count += 1 # milestone 8 : adding score_count

        # Milestone #5: Generate new food
        food_x, food_y, food_id = new_food(canvas)
        #return food_x, food_y, food_id, True  # just_ate = True
        return food_x, food_y, food_id, score_count, True  # just_ate = True # milestone 8 : adding score_count

    else:
        #return food_x, food_y, food_id, False  # just_ate = False
        return food_x, food_y, food_id, score_count, False  # just_ate = False # milestone 8 : adding score_count


# functions for Milestone #5      
def new_food(canvas):
    food_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
    food_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
    food_id = draw_food(canvas,food_x,food_y,"red") 

    return food_x, food_y, food_id   

# functions for Milestone #7
#def show_animated_game_over(canvas):

# milestone 8 : adding score_count 
def show_animated_game_over(canvas, score_count):
    size = 32
    grow = True

    # Draw the button once
    button_bounds = show_play_again_button(canvas)
    x1, y1, width, height = button_bounds
    x2 = x1 + width
    y2 = y1 + height

    while True:
        canvas.clear()  # Clear everything each frame
        # Draw the pulsing "Game Over"
        canvas.create_text(
            CANVAS_WIDTH // 4,
            CANVAS_HEIGHT // 2,
            text="Game Over!",
            font="Arial",
            font_size=size,
            color="red"
        )
        
        # show final score
        canvas.create_text(
            CANVAS_WIDTH // 4,
            CANVAS_HEIGHT // 3,
            text="Your score is " + str(score_count)+ " !",
            font="Arial",
            font_size=size//2,
            color="blue"
        )
         
        # Draw button again (since we cleared everything)
        canvas.create_rectangle(x1, y1, x2, y2, color="lightgray")
        canvas.create_text(
            x1 + width // 5,
            y1 + height // 3,
            text="Play Again",
            font="Arial",
            font_size=16,
            color="black"
        )

        size += 2 if grow else -2
        if size >= 48 or size <= 28:
            grow = not grow
        

    # Check if user clicked "Play Again"
        click = canvas.get_last_click()
        if click is not None:
            click_x, click_y = click
            if x1 <= click_x <= x2 and y1 <= click_y <= y2:
                print("Restarting game...")
                canvas.clear()
                main()
                return

        time.sleep(0.1)

def show_play_again_button(canvas):
    button_width = 120
    button_height = 40
    #button_x = CANVAS_WIDTH // 2 - 60
    button_x = CANVAS_WIDTH // 2 - button_width // 2
    #button_y = CANVAS_HEIGHT // 2 + 50
    button_y = CANVAS_HEIGHT*3//4

    canvas.create_rectangle(
        button_x, button_y,
        button_x + button_width, button_y + button_height,
        color="lightgray"
    )
    
    canvas.create_text(
        button_x + button_width // 5,
        button_y + button_height // 3,
        text="Play Again",
        font="Arial",
        font_size=16,
        color="black"
    )

    return (button_x, button_y, button_width, button_height)

# milestone 9: "showing the start screen and having different levels
def show_start_screen(canvas):
    canvas.clear()
    canvas.create_text(
        (CANVAS_WIDTH // 2)/10,
        CANVAS_HEIGHT // 4,
        text="🐍 Sewar's Snake Game 🐍",
        font="Arial",
        font_size=28,
        color="darkgreen"
    )

    canvas.create_text(
        CANVAS_WIDTH // 4,
        CANVAS_HEIGHT // 4 + 40,
        text="Choose your difficulty level:",
        font="Arial",
        font_size=18,
        color="black"
    )

    # Buttons for levels
    levels = [("Easy", 0.2), ("Medium", 0.1), ("Hard", 0.05)]
    buttons = []

    for i, (label, delay) in enumerate(levels):
        btn_width, btn_height = 100, 40
        x1 = CANVAS_WIDTH // 2 - btn_width // 2
        y1 = CANVAS_HEIGHT // 2 + i * (btn_height + 10)
        x2 = x1 + btn_width
        y2 = y1 + btn_height
        canvas.create_rectangle(x1, y1, x2, y2, color="turquoise ")
        canvas.create_text(
            (x1 + x2) // 2 - btn_width/4  ,
            (y1 + y2) // 2 - btn_height/5 ,
            text=label,
            font="Arial",
            font_size=16,
            color="black"
        )
        buttons.append((x1, y1, x2, y2, delay))

    # Wait for click
    while True:
        click = canvas.get_last_click()
        if click:
            x, y = click
            for x1, y1, x2, y2, delay in buttons:
                if x1 <= x <= x2 and y1 <= y <= y2:
                    return delay
        time.sleep(0.1)

if __name__ == '__main__':
    main()
