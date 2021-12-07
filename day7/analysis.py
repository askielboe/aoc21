import numpy as np

crabs = np.loadtxt("crabs.txt", delimiter=',')

# Question 1
alignment = np.median(crabs)
dist = np.abs(crabs - alignment)
fuel = np.sum(dist)
print("fuel = ", fuel)

# Question 2
def fuel_from_dist(dist):
    return dist * (dist + 1.) / 2.

min_fuel = np.sum(fuel_from_dist(np.max(crabs))) * len(crabs)
for d in range(int(np.max(crabs))):
    dist = np.abs(crabs - d)
    fuel = np.sum(fuel_from_dist(dist))
    if fuel < min_fuel:
        min_fuel = fuel
        print("new min: ", min_fuel)

