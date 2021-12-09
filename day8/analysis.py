import re
from tqdm import tqdm
import random
import numpy as np


def multireplace(string, replacements, ignore_case=False):
    """
    Given a string and a replacement map, it returns the replaced string.
    :param str string: string to execute replacements on
    :param dict replacements: replacement dictionary {value to find: value to replace}
    :param bool ignore_case: whether the match should be case insensitive
    :rtype: str
    """
    if not replacements:
        # Edge case that'd produce a funny regex and cause a KeyError
        return string

    # If case insensitive, we need to normalize the old string so that later a replacement
    # can be found. For instance with {"HEY": "lol"} we should match and find a replacement for "hey",
    # "HEY", "hEy", etc.
    if ignore_case:
        def normalize_old(s):
            return s.lower()

        re_mode = re.IGNORECASE

    else:
        def normalize_old(s):
            return s

        re_mode = 0

    replacements = {normalize_old(key): val for key, val in replacements.items()}

    # Place longer ones first to keep shorter substrings from matching where the longer ones should take place
    # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against the string 'hey abc', it should produce
    # 'hey ABC' and not 'hey ABc'
    rep_sorted = sorted(replacements, key=len, reverse=True)
    rep_escaped = map(re.escape, rep_sorted)

    # Create a big OR regex that matches any of the substrings to replace
    pattern = re.compile("|".join(rep_escaped), re_mode)

    # For each match, look up the new string in the replacements, being the key the normalized old string
    return pattern.sub(lambda match: replacements[normalize_old(match.group(0))], string)


unique_segments_per_digit = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}

patterns = []
outputs = []

with open("input.txt", 'r') as file:
    for line in file.readlines():
        p, o = line.split(" | ")
        patterns.append(p.split(" "))
        outputs.append(o.rstrip("\n").split(" "))

# Question 1
count = 0
for output in outputs:
    for digit_len in [len(v) for v in output]:
        if digit_len in unique_segments_per_digit.values():
            count += 1

# Question 2
alphabet = {
     "abcefg": "0",
     "cf": "1",       # unique
     "acdeg": "2",
     "acdfg": "3",
     "bcdf": "4",     # unique
     "abdfg": "5",
     "abdefg": "6",
     "acf": "7",      # unique
     "abcdefg": "8",  # unique
     "abcdfg": "9"
}

chars = ["a", "b", "c", "d", "e", "f", "g"]

identity_cipher = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
    "e": "e",
    "f": "f",
    "g": "g",
}


def shuffle(l):
    l2 = l[:]
    random.shuffle(l2)
    return l2


def sort(s):
    s2 = list(s)
    s2.sort()
    return "".join(s2)


def decode(pattern, cipher):
    return multireplace(pattern, cipher)


def random_cipher():
    return {k: v for k, v in zip(chars, shuffle(chars))}


def to_digit(pattern, cipher):
    return alphabet[sort(decode(pattern, cipher))]


pattern = patterns[0]
output = outputs[0]


def crack(pattern, output):
    while True:
        cipher = random_cipher()
        decoded_patterns = [sort(decode(p, cipher)) for p in pattern]
        if np.all([p in alphabet.keys() for p in decoded_patterns]):
            print(f"found cipher: {cipher}")
            digits = ''.join([to_digit(o, cipher) for o in output])
            print(f"digits: {digits}")
            return int(digits)

digits = []


for i in tqdm(range(len(patterns))):
    digits.append(crack(patterns[i], outputs[i]))

result = np.sum(digits)
print(f"result: {result}")
