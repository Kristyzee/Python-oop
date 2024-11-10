import turtle
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def draw(self, ax):
        circle = patches.Circle((0, 0), self.radius, edgecolor='black', facecolor=self.color)
        ax.add_patch(circle)
        ax.set_xlim(-self.radius-1, self.radius+1)
        ax.set_ylim(-self.radius-1, self.radius+1)
        ax.set_aspect('equal')

class Square(Shape):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size

    def draw(self, ax):
        square = patches.Rectangle((-self.size/2, -self.size/2), self.size, self.size, edgecolor='black', facecolor=self.color)
        ax.add_patch(square)
        ax.set_xlim(-self.size/2-1, self.size/2+1)
        ax.set_ylim(-self.size/2-1, self.size/2+1)
        ax.set_aspect('equal')

class Octagon(Shape):
    def __init__(self, size, color):
        super().__init__(color)
        self.size = size
        self.color = color

    def draw(self, ax):
        octagon = patches.RegularPolygon((0, 0), numVertices=8, radius=self.size, facecolor=self.color)
        ax.add_patch(octagon)
        ax.set_xlim(-self.size-1, self.size+1)
        ax.set_ylim(-self.size-1, self.size+1)
        ax.set_aspect('equal')

def main():
    print("Choose a shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Octagon")

    choice = input("Enter your choice (1/2/3 or Circle/Square/Octagon): ").strip().lower().capitalize()

    shape_map = {
        "1": "Circle",
        "2": "Square",
        "3": "Octagon",
        "Circle": "Circle",
        "Square": "Square",
        "Octagon": "Octagon"
    }

    if choice in shape_map:
        fig, ax = plt.subplots()
        ax.set_axis_off()

        if shape_map[choice] == "Circle":
            radius = int(input("Enter radius: "))
            color = input("Enter color: ").capitalize()
            shape = Circle(radius, color)
        elif shape_map[choice] == "Square":
            size = int(input("Enter size: "))
            color = input("Enter color: ").capitalize()
            shape = Square(size, color)
        elif shape_map[choice] == "Octagon":
            size = int(input("Enter size: "))
            color = input("Enter color: ").capitalize()
            shape = Octagon(size, color)

        shape.draw(ax)
        plt.show()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()