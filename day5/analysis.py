import numpy as np
import matplotlib.pyplot as plt


# question 1
m = np.zeros([1000, 1000])
with open("lines.txt", "r") as file:
    for line in file.readlines():
        xy1, xy2 = line.split(" -> ")
        x1, y1 = xy1.split(",")
        x2, y2 = xy2.split(",")

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        # Ignore directions
        if x1 > x2:
            x1old = x1
            x1 = x2
            x2 = x1old

        if y1 > y2:
            y1old = y1
            y1 = y2
            y2 = y1old

        # Only horizontal or vertical
        if x1 != x2 and y1 != y2:
            continue

        n = np.zeros([1000, 1000])

        print(f"({x1}, {y1}) -> ({x2}, {y2})")

        if x1 == x2:
            n[x1, y1:y2+1] = 1
        if y1 == y2:
            n[x1:x2+1, y1] = 1

        m += n

plt.imshow(m)
plt.savefig("m.png")

print("\n")
print(np.sum(m >= 2))

# question 2
fig = plt.figure()
m = np.zeros([1000, 1000])
with open("lines.txt", "r") as file:
    for line in file.readlines():
        xy1, xy2 = line.split(" -> ")
        x1, y1 = xy1.split(",")
        x2, y2 = xy2.split(",")

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        n = np.zeros([1000, 1000])

        print(f"({x1}, {y1}) -> ({x2}, {y2})")

        # Horizontal or vertical
        if x1 == x2 or y1 == y2:
            # Ignore directions
            if x1 > x2:
                x1old = x1
                x1 = x2
                x2 = x1old

            if y1 > y2:
                y1old = y1
                y1 = y2
                y2 = y1old

            if x1 == x2:
                n[x1, y1:y2+1] = 1
            elif y1 == y2:
                n[x1:x2+1, y1] = 1
        else:
            for i in range(abs(x2-x1)+1):
                j = i
                if x1 > x2:
                    i = -1 * i
                if y1 > y2:
                    j = -1 * j
                print(i, j, x1+i, y1+j)
                n[x1+i, y1+j] = 1

        m += n

plt.imshow(m)
plt.savefig("m2.png")

print("\n")
print(np.sum(m >= 2))
