import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
    # cmap=plt.cm.Blues, edgecolor="none", s=1)
    plt.scatter(rw.x_values, rw.y_values, c="red",
                cmap=plt.cm.Blues, edgecolor="none", s=1)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.show()
    plt.savefig("./walk.svg")
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
