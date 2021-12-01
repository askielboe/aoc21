import numpy as np
scan = np.loadtxt("scan.txt")

# 1
result = len([s for s in np.diff(scan) if s > 0])

# 2
conv = np.convolve(scan, [1, 1, 1], mode="valid")
result = len([s for s in np.diff(conv) if s > 0])
