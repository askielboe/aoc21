import numpy as np

fish = np.loadtxt("fish.txt", delimiter=',')

# Question 2
def tick(fish):
    fish -= 1
    spawners = fish == -1
    fish[spawners] = 6
    return np.concatenate([fish, 8 * np.ones(np.sum(spawners))])

for i in range(80):
    fish = tick(fish)
    print(i, fish.shape)

print(len(fish))


# Question 2
fish = np.loadtxt("fish.txt", delimiter=',')
hist, bins = np.histogram(fish, range(10))


def tick(hist):
    spawners = hist[0]
    hist = np.append(hist[1:], spawners)
    hist[6] += spawners
    return hist


for i in range(256):
    hist = tick(hist)

print(sum(hist))
