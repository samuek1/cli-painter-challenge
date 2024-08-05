# TODO: Add code here

import matplotlib.pyplot as plt
import json

class Point:
def __init__(self, x: float, y: float):
self.x = x
self.y = y

def __repr__(self):
return f"({self.x}, {self.y})"

class Circle:
def __init__(self, center: Point, radius: float):
self.center = center
self.radius = radius

def area(self) -> float:
return 3.14159 * (self.radius ** 2)

def draw(self):
circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
plt.gca().add_patch(circle)
plt.axis("scaled")
plt.show()

class Triangle:
def __init__(self, point_1: Point, point_2: Point, point_3: Point):
self.point_1 = point_1
self.point_2 = point_2
self.point_3 = point_3

def area(self) -> float:
x1, y1 = self.point_1.x, self.point_1.y
x2, y2 = self.point_2.x, self.point_2.y
x3, y3 = self.point_3.x, self.point_3.y
return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

def draw(self):
x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
plt.fill(x, y, color='b', edgecolor='black')
plt.axis("scaled")
plt.show()


class Rectangle:
def __init__(self, point_1, point_2):
self.point_1 = point_1
self.point_2 = point_2

def area(self):
width = abs(self.point_2.x - self.point_1.x)
height = abs(self.point_2.y - self.point_1.y)
return float(width * height)

def draw(self):
x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
plt.fill(x, y, color='g')
plt.axis("scaled")
plt.show()

def __str__(self):
return f"Rectangle with opposite vertices at ({self.point_1.x}, {self.point_1.y}) and ({self.point_2.x}, {self.point_2.y})"

if __name__ == "__main__":
p1 = Point(1, 2)
p2 = Point(4, 5)
rect = Rectangle(p1, p2)

print(rect)
print(f"Area: {rect.area()}")
rect.draw()
class Painter:
FILE = ".painter"

def __init__(self) -> None:
self.shapes = []
self._load()

def _load(self) -> None:
try:
with open(self.FILE, 'r') as file:
data = json.load(file)
for shape_data in data:
if shape_data["type"] == "Circle":
center = Point(shape_data["center"]["x"], shape_data["center"]["y"])
radius = shape_data["radius"]
self.shapes.append(Circle(center, radius))
elif shape_data["type"] == "Triangle":
point1 = Point(shape_data["point1"]["x"], shape_data["point1"]["y"])
point2 = Point(shape_data["point2"]["x"], shape_data["point2"]["y"])
point3 = Point(shape_data["point3"]["x"], shape_data["point3"]["y"])
self.shapes.append(Triangle(point1, point2, point3))
elif shape_data["type"] == "Rectangle":
point1 = Point(shape_data["point1"]["x"], shape_data["point1"]["y"])
point2 = Point(shape_data["point2"]["x"], shape_data["point2"]["y"])
self.shapes.append(Rectangle(point1, point2))
except FileNotFoundError:
print("Archivo no encontrado:", self.FILE)
except json.JSONDecodeError:
print("Error al decodificar el archivo JSON.")

def draw_all(self):
for shape in self.shapes:
if isinstance(shape, Rectangle):
shape.draw(show=False)
else:
shape.draw()
plt.show()


center = Point(0.0, 0.0)
circle = Circle(center, 5.0)
print(f"Área del círculo: {circle.area():.2f}")
circle.draw()
