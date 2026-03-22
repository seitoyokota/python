import curses, random,time #curses is a library for creating text-based user interfaces, random is used for generating random numbers, and time is used for adding delays in the game.
s=curses.initscr() #Initialize the curses library and return a window object representing the entire screen.
curses.curs_set(0) #Hide the cursor on the screen
height,width=s.getmaxyx() #Get the height and width of the window. getmaxyx() returns a tuple (height, width) representing the dimensions of the window.
window=curses.newwin(height,width,0,0) #Create a new window with the specified height and width, and position it at the top-left corner of the screen (0, 0).
window.keypad(1) #Enable the keypad mode for the window, allowing it to capture special keys like arrow keys.
window.timeout(100) #Set a timeout for the window's getch() method. This means that if no key is pressed within 100 milliseconds, getch() will return -1, allowing the game loop to continue even when no input is received.
snake=[[height//2,width//2],[height//2,width//2-1],[height//2,width//2-2]] #Initialize the snake's position as a list of coordinates.
food=[random.randint(1,height-2),random.randint(1,width-2)] #Generate a random position for the food within the boundaries of the window, ensuring it does not appear on the borders.
window.addch(food[0],food[1],ord('o')) #Add the food character 'o' to the window at the generated food position. ord('o') converts the character 'o' to its corresponding ASCII value, which is required by the addch() method to display the character on the screen.
k=curses.KEY_RIGHT #Initialize the direction of the snake's movement to the right by setting k to curses.KEY_RIGHT, which represents the right arrow key. This will be used to control the snake's movement in the game loop.
while 1:
    nk = window.getch() #Wait for user input and store the key pressed in the variable nk. The getch() method captures a single key press from the user.
    k = nk if nk in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT] else k #Update the direction of the snake's movement based on the key pressed by the user. If the key pressed is one of the arrow keys (up, down, left, right), update k to that key. Otherwise, keep k unchanged, allowing the snake to continue moving in its current direction.
    head2=snake[0][0]+(k==curses.KEY_DOWN)-(k==curses.KEY_UP) #Calculate the new head position of the snake based on the current direction of movement. If k is curses.KEY_DOWN, add 1 to the current head's row coordinate; if k is curses.KEY_UP, subtract 1 from the current head's row coordinate. This determines the new vertical position of the snake's head.
    width2=snake[0][1]+(k==curses.KEY_RIGHT)-(k==curses.KEY_LEFT) #Calculate the new head position of the snake based on the current direction of movement. If k is curses.KEY_RIGHT, add 1 to the current head's column coordinate; if k is curses.KEY_LEFT, subtract 1 from the current head's column coordinate. This determines the new horizontal position of the snake's head.
    if head2 in [0,height] or width2 in [0,width] or [head2,width2] in snake: #Check for collision conditions. If the new head position (head2, width2) is outside the boundaries of the window (i.e., row coordinate is 0 or height, or column coordinate is 0 or width) or if the new head position collides with any part of the snake's body (i.e., it is already in the snake list), then the game is over
        break
    snake.insert(0,[head2,width2]) #Insert the new head position at the beginning of the snake list, effectively moving the snake in the current direction.
    if snake[0]==food:
        food=[random.randint(1,height-2),random.randint(1,width-2)] #If the snake's head is at the same position as the food, generate a new random position for the food within the boundaries of the window, ensuring it does not appear on the borders.
        while food in snake: 
            food=[random.randint(1,height-2),random.randint(1,width-2)] #Ensure that the new food position does not collide with the snake's body. If the generated food position is already occupied by the snake, keep generating new positions until a valid one is found.
        window.addch(food[0],food[1],ord('o')) #Add the new food character 'o' to the window at the generated food position.
    else:
        t=snake.pop() #If the snake did not eat food, remove the last segment of the snake's body (the tail) to maintain the same length as it moves.
        window.addch(t[0],t[1],' ') #Add a space character at the position of the removed tail segment to visually erase it from the window, giving the appearance of the snake moving forward.
    window.addch(snake[0][0],snake[0][1],ord('*'))  #Add the snake's head character '@' to the window at the new head position, visually representing the snake's movement on the screen.
curses.endwin() #Terminate the curses application and return the terminal to its normal state.
print("Game Over. Score:",len(snake)-3) #After the game loop ends (when the snake collides with a wall or itself), print a "Game Over" message along with the player's score, which is calculated as the length of the snake minus 3 (the initial length of the snake). 