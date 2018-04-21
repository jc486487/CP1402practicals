import random

picks = int(input("How many quick picks? "))
MIN = 1
MAX = 45

tgt = []
for x in range(0, picks, 1):
    tgt = []
    for num in range(0, 6, 1):
        value = random.randint(MIN, MAX)
        if value not in tgt:
            tgt.append(value)
    tgt.sort()
    print(" ".join(map(str, tgt)))
