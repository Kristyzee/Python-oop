# import pygame
# import random

# # Initialize pygame
# pygame.init()

# # Define constants
# WIDTH, HEIGHT = 800, 600
# SQUARE_SIZE = 50

# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # List of possible colors for the squares
# COLORS = [
#     (255, 0, 0),   # Red
#     (0, 255, 0),   # Green
#     (0, 0, 255),   # Blue
#     (255, 255, 0), # Yellow
#     (255, 165, 0), # Orange
#     (138, 43, 226),# BlueViolet
#     (255, 192, 203) # Pink
# ]

# # Define the Square class
# class Square:
#     def __init__(self, x, y, size, color):
#         self.x = x
#         self.y = y
#         self.size = size
#         self.color = color
    
#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# # Function to generate random squares
# def create_random_squares(n):
#     squares = []
#     for _ in range(n):
#         x = random.randint(0, WIDTH - SQUARE_SIZE)
#         y = random.randint(0, HEIGHT - SQUARE_SIZE)
#         color = random.choice(COLORS)
#         square = Square(x, y, SQUARE_SIZE, color)
#         squares.append(square)
#     return squares

# # Main function
# def main():
#     # Set up the screen
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption('Random Squares')

#     # Set up the clock
#     clock = pygame.time.Clock()

#     # Create random squares
#     n = 10  # Number of squares to draw
#     squares = create_random_squares(n)

#     # Main loop
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Fill the screen with a white background
#         screen.fill(WHITE)

#         # Draw all the squares
#         for square in squares:
#             square.draw(screen)

#         # Update the display
#         pygame.display.flip()

#         # Cap the frame rate
#         clock.tick(60)

#     # Quit pygame
#     pygame.quit()

# if __name__ == '__main__':
#     main()





import pygame
import random

# Initialize pygame
pygame.init()

# Define constants for the window size
WIDTH, HEIGHT = 800, 600

# List of possible colors for the squares
COLORS = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (255, 165, 0), # Orange
    (138, 43, 226),# BlueViolet
    (255, 192, 203) # Pink
]

# Square class to define properties of each square
class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
    def draw(self, screen):
        """Draw the square on the screen"""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Function to get user input for number of squares
def get_number_of_squares():
    while True:
        try:
            n = int(input("Enter the number of squares to display: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Function to get user input for the square size
def get_square_size():
    while True:
        try:
            size = int(input("Enter the size of each square: "))
            if size <= 0:
                print("Please enter a positive integer for size.")
            else:
                return size
        except ValueError:
            print("Invalid input! Please enter a valid integer for size.")

# Function to generate squares with random colors
def create_random_squares(n, size):
    squares = []
    for _ in range(n):
        x = random.randint(0, WIDTH - size)  # Ensure square stays within the window
        y = random.randint(0, HEIGHT - size)
        color = random.choice(COLORS)  # Randomly choose a color for each square
        square = Square(x, y, size, color)
        squares.append(square)
    return squares

# Main function to initialize the game
def main():
    # Get user input for the number of squares, square size, and color
    n = get_number_of_squares()
    size = get_square_size()

    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Random Squares')

    # Set up the clock for FPS control
    clock = pygame.time.Clock()

    # Create random squares with random colors
    squares = create_random_squares(n, size)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a white background
        screen.fill((255, 255, 255))

        # Draw all the squares
        for square in squares:
            square.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

    # Quit pygame
    pygame.quit()

# Run the main function
if __name__ == "__main__":
    main()
