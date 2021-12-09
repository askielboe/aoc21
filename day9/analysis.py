import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

plt.figure()

DIM = 100

height = np.empty((DIM, DIM), dtype=int)

with open("height.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        row = [int(n) for n in list(line.rstrip("\n"))]
        height[i] = row

plt.imshow(height)
plt.savefig("height.png")

# Question 1
kernel = np.array(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
    ]
)  # flip this in horizontal and vertical plane

minmap = np.ones((DIM, DIM))
for i in range(4):
    conv = ndimage.convolve(height, kernel, mode="constant", cval=10)
    minmap *= conv < 0
    kernel = np.rot90(kernel)

plt.imshow(minmap)
plt.savefig("minmap.png")

riskmap = (height + 1) * minmap
total_risk = np.sum(riskmap)
print(f"total_risk = {total_risk}")

# Question 2
minmap_loc_x = np.where(minmap == 1)[0]
minmap_loc_y = np.where(minmap == 1)[1]
minima = [(x, y) for x, y in zip(minmap_loc_x, minmap_loc_y)]

basins = []
checked = []
for minimum in tqdm(minima):
    basin = []
    queue = [minimum]
    while len(queue) > 0:
        x, y = queue.pop()
        checked.append((x, y))
        if (x, y) not in basin and height[x, y] < 9:
            basin.append((x, y))
            neighbors = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ]
            for x, y in neighbors:
                x = min(max(x, 0), DIM - 1)
                y = min(max(y, 0), DIM - 1)
                if (x, y) not in checked:
                    queue.append((x, y))
    basins.append(basin)

basinsizes = {i: len(basins[i]) for i in range(len(basins))}
sorted_basinsizes = sorted(basinsizes.items(), key=lambda x: x[1])

result = np.product(
    [
        sorted_basinsizes[-1][1],
        sorted_basinsizes[-2][1],
        sorted_basinsizes[-3][1],
    ]
)
