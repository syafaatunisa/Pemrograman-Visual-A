import matplotlib.pyplot as plt

class HorizontalLine:
    def __init__(self, y, x1, x2):
        self.y = y
        self.x1 = x1
        self.x2 = x2

    def plot(self):
        plt.plot([self.x1, self.x2], [self.y, self.y], marker='o')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Plot of a Horizontal Line')
        plt.grid(True)
        plt.show()

# Membuat objek garis horizontal dengan sumbu y di 4 dan titik awal pada x=2 dan titik akhir pada x=7
horizontal_line = HorizontalLine(4, 2, 7)
horizontal_line.plot()
