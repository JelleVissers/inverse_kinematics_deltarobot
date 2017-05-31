# Note this program is a beta version and does not provide accurate results for visualization.

import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class draw:
    def __init__(self):
        self.fig = plt.figure("delta")
        self.ax  = p3.Axes3D(self.fig)

    def draw_line(self):
        self.x = [100,-50,-50,100]
        self.y = [0,86.6025403784,-86.6025403784,0]
        self.z = [0,0,0,0]

        plt.plot(self.x,self.y,self.z)

    def show(self):
        plt.show()


def main():
    graph = draw()
    graph.draw_line()
    graph.show()

if __name__ == '__main__':
    main()
