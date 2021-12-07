import numpy as np

# input
raw_moves = np.loadtxt("moves.txt", dtype=(str, int))
moves = {
    inst: [int(v) for (k, v) in raw_moves if k == inst]
    for inst in ["fo", "up", "do"]
}

# 1
forward = np.sum(moves["fo"])
depth = np.sum(moves["do"]) - np.sum(moves["up"])
result = forward * depth

# 2
forward = 0
depth = 0
aim = 0
for k, v in raw_moves:
    v = int(v)
    if k == "fo":
        forward += v
        depth += aim * v
    if k == "up":
        aim -= v
    if k == "do":
        aim += v

result = forward * depth