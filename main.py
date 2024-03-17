import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt

def distanceOfPoints(point1: dict, point2: dict):
    Tsik = np.sqrt(np.abs(point1['x'] - point2['x'])**2 + np.abs(point1['y'] - point2['y'])**2)
    Tter = np.sqrt(Tsik**2 + np.abs(point1['z'] - point2['z']))
    return Tter

pearls = []
with open('gyongyok.txt') as f:
    data = f.read()
    lines = data.split('\n')[1:]
    pearls = []
    for line in lines:
        values = line.split(';')
        distFromOrigo = distanceOfPoints({'x': 0, 'y': 0, 'z': 0}, {'x': int(values[0]), 'y': int(values[1]), 'z': int(values[2])})
        pearl = {'x': int(values[0]), 'y': int(values[1]), 'z': int(values[2]), 'price': int(values[3]), 'distFromOrigo': distFromOrigo}
        pearls.append(pearl)

prices = [pearl['price'] for pearl in pearls]
sizes = [pearl['price'] * 10 for pearl in pearls]

x_coords = [pearl['x'] for pearl in pearls]
y_coords = [pearl['y'] for pearl in pearls]
z_coords = [pearl['z'] for pearl in pearls]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, s=sizes)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gyöngyvadászat')

selected_points = np.random.choice(pearls, size=5, replace=False)

x_selected = [point['x'] for point in selected_points]
y_selected = [point['y'] for point in selected_points]
z_selected = [point['z'] for point in selected_points]

line, = ax.plot(x_selected, y_selected, z_selected, color='red')

line_to_origin, = ax.plot([x_selected[-1], 0], [y_selected[-1], 0], [z_selected[-1], 0], color='blue')

def update(frame):
    line.set_data_3d(x_selected[:frame+1], y_selected[:frame+1], z_selected[:frame+1])
    line_to_origin.set_data_3d([x_selected[frame], 0], [y_selected[frame], 0], [z_selected[frame], 0])

animation = FuncAnimation(fig, update, frames=len(x_selected), interval=700, repeat=True)

ax.view_init(elev=-90, azim=0)

plt.show()