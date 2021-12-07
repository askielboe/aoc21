import numpy as np

bits_as_str = np.loadtxt("bits.txt", dtype=str)
bits_as_lst = np.array([list(s) for s in bits_as_str], dtype=np.uint)

# question 1
col_sum = np.sum(bits_as_lst, axis=0)
col_len = len(bits_as_lst)

# most common bit
gamma_rate_b = (col_sum > 0.5 * col_len).astype(np.uint)
gamma_rate_d = int("".join(gamma_rate_b.astype(str)), 2)

# least common bit
epsilon_rate_b = (col_sum < 0.5 * col_len).astype(np.uint)
epsilon_rate_d = int("".join(epsilon_rate_b.astype(str)), 2)

power_consuption = gamma_rate_d * epsilon_rate_d

print(gamma_rate_d)
print(epsilon_rate_d)
print(power_consuption)

# question 2
data = bits_as_lst
col = 0
while len(data) > 1:
    most_common_bit = int(np.sum(data[:, col]) >= 0.5 * len(data))
    data = data[data[:, col] == most_common_bit]
    print(col, most_common_bit)
    col += 1
oxygen_generator_rating = int("".join(data[0].astype(str)), 2)

data = bits_as_lst
col = 0
while len(data) > 1:
    least_common_bit = int(np.sum(data[:, col]) < 0.5 * len(data))
    data = data[data[:, col] == least_common_bit]
    print(col, least_common_bit)
    col += 1
co2_scrubber_rating = int("".join(data[0].astype(str)), 2)

print(oxygen_generator_rating)
print(co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)