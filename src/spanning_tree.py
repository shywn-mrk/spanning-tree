import matplotlib.pyplot as plt
from matplotlib import lines
import sys
from math import sqrt

def print_spanning_tree(points):
    x_list = []
    y_list = []

    for (x, y) in points:
        x_list.append(x)
        y_list.append(y)

    plt.plot(x_list, y_list, 'ro')

    reached = []
    unreached = [] + points

    reached.append(unreached[0])
    unreached.pop(0)

    while len(unreached) > 0:
        record = sys.maxsize
        r_index = None
        u_index = None
        
        for i in range(len(reached)):
            for j in range(len(unreached)):
                x = (reached[i][0] - unreached[j][0])
                y = (reached[i][1] - unreached[j][1])
                distance = sqrt(x ** 2 + y ** 2)

                if distance < record:
                    record = distance
                    r_index = i
                    u_index = j
        
        line = lines.Line2D(
            [reached[r_index][0], unreached[u_index][0]],
            [reached[r_index][1], unreached[u_index][1]]
        )
        plt.axes().add_line(line)

        reached.append(unreached[u_index])
        unreached.pop(u_index)

    plt.show()
