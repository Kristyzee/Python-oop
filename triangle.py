# import turtle
# import random

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor(random.choice(['black', 'maroon', 'gray', 'lightblue', 'beige','red',' yellow']))  # Random background color

# # Create a turtle object
# t = turtle.Turtle()
# t.speed(3)  # Set drawing speed to the fastest

# # Function to draw a triangle with a random color

# def draw_triangle():
#     # Choose a random color for the triangle
#     triangle_color = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink'])
#     t.fillcolor(triangle_color)
#     t.begin_fill()
    
#     # Draw a triangle
#     for _ in range(3):
#         t.forward(100)
#         t.right(120)
    
#     t.end_fill()

# # Set the initial position for the first triangle
# t.penup()
# t.setpos(-70, 200)  # Start at the top of the screen
# t.pendown()

# # Draw 4 triangles vertically with random colors
# for i in range(4):
#     draw_triangle()
#     t.penup()
#     t.setpos(-70, 200 - (i + 1) * 100)  # Move down for the next triangle
#     t.pendown()

# # Hide the turtle and display the result
# t.hideturtle()
# screen.mainloop()





# import turtle
# import random

# # Define a class to handle the turtle drawing
# class TriangleDrawer:
#     def __init__(self):
#         # Set up the screen
#         self.screen = turtle.Screen()
#         self.screen.bgcolor(random.choice(['black', 'maroon', 'gray', 'lightblue', 'beige', 'red', 'yellow']))  # Random background color
        
#         # Create a turtle object
#         self.t = turtle.Turtle()
#         self.t.speed(3)  # Set drawing speed to the fastest

#     def draw_triangle(self, x, y):
#         """Draw a triangle at the specified position with a random color."""
#         # Choose a random color for the triangle
#         triangle_color = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink'])
#         self.t.fillcolor(triangle_color)

#         # Move to the position without drawing
#         self.t.penup()
#         self.t.setpos(x, y)
#         self.t.pendown()

#         # Begin drawing the triangle
#         self.t.begin_fill()
#         for _ in range(3):
#             self.t.forward(100)
#             self.t.right(120)
#         self.t.end_fill()

#     def draw_stacked_triangles(self):
#         """Draw 4 stacked triangles with random colors."""
#         start_x = -70
#         start_y = 200
#         for i in range(4):
#             self.draw_triangle(start_x, start_y - (i * 100))  # Draw triangle at each new position

#     def run(self):
#         """Start the drawing process."""
#         self.draw_stacked_triangles()
#         self.t.hideturtle()
#         self.screen.mainloop()

# # Create an instance of TriangleDrawer and run the drawing
# triangle_drawer = TriangleDrawer()
# triangle_drawer.run()






import turtle
import random

# Define a class to handle the turtle drawing
class TriangleDrawer:
    def __init__(self):  # Corrected constructor
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.bgcolor(self.random_color())  # Set random background color

        # Create a turtle object
        self.t = turtle.Turtle()
        self.t.speed(3)  # Set drawing speed to the fastest

    def random_color(self):
        """Generate a random RGB color as a string."""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02x}{g:02x}{b:02x}"  # Return color as a hex string

    def draw_triangle(self, x, y):
        """Draw a triangle at the specified position with random fill and pen colors."""
        # Set random fill and pen colors
        self.t.fillcolor(self.random_color())
        self.t.pencolor(self.t.fillcolor())

        # Move to the position without drawing
        self.t.penup()
        self.t.setpos(x, y)
        self.t.pendown()

        # Begin drawing the triangle
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(100)
            self.t.right(120)  # Turn left by 120 degrees to make a triangle
        self.t.end_fill()

    def draw_stacked_triangles(self):
        """Draw 4 stacked triangles with random colors."""
        start_x = -70
        start_y = 200
        for i in range(4):
            self.draw_triangle(start_x, start_y - (i * 100))  # Draw triangle at each new position

    def run(self):
        """Start the drawing process."""
        self.draw_stacked_triangles()
        self.t.hideturtle()  # Hide the turtle after drawing
        self.screen.mainloop()  # Keep the window open

# Create an instance of TriangleDrawer and run the drawing
triangle_drawer = TriangleDrawer()
triangle_drawer.run()
