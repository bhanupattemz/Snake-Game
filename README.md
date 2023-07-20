# Snake-Game
Snake Game by Turtle graphics in python
The provided Python code is a simple implementation of the classic Snake game using the Turtle module, a graphics library in Python. The game consists of a snake that moves around the screen, trying to eat food items to grow longer. The player controls the snake's direction using arrow keys.

Components:

1. `food.py`: Defines the `Food` class, representing the food item the snake must eat to grow. The food appears as a blue circle, and its position changes randomly within the game window.

2. `score_bord.py`: Contains the `Score` class to manage and display the player's score. The highest score achieved during gameplay is stored and updated in a separate data file named `data.txt`.

3. `snake.py`: Implements the `Snake` class to create and control the snake. The snake consists of linked segments, which increase in number as the snake eats food.

4. `main.py`: The main script that brings everything together. It sets up the game window, initializes the snake, food, and score objects. The game loop continuously updates the screen, handles player input, and checks for collisions (e.g., when the snake hits the screen boundary or collides with itself). When a collision occurs, the game resets the score and the snake's position.

The game continues running until the player chooses to exit.
