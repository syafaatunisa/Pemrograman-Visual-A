import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def plot(self):
        plt.plot([self.start_point.x, self.end_point.x], [self.start_point.y, self.end_point.y], marker='o')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Plot of a Line')
        plt.grid(True)
        plt.show()

def create_point(x, y):
    return Point(x, y)

def create_line(point1, point2):
    return Line(point1, point2)

# Membuat titik A dengan koordinat (2, 3)
point_A = create_point(2, 3)

# Membuat titik B dengan koordinat (5, 7)
point_B = create_point(5, 7)

# Membuat garis dari titik A ke titik B
line_AB = create_line(point_A, point_B)

# Mengatur warna latar belakang menjadi hitam
plt.figure().patch.set_facecolor('black')

# Plot garis
line_AB.plot()
