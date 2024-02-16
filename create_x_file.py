import os
import random
import sys

from tqdm import tqdm

n = int(
    input("Number of random integers to generate: ").strip() or 100
)  # Default value is 100

random_integers = [random.randint(1, sys.maxsize) for _ in tqdm(range(n))]

with open(os.path.join("data", "random_integers.txt"), "w", encoding="utf-8") as f:
    for integer in random_integers:
        f.write(str(integer) + "\n")

print(f"{n} random integers have been generated and saved to random_integers.txt")
