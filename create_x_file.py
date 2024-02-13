import random
import sys

# Generate 1000 random integers
random_integers = [random.randint(1, sys.maxsize) for _ in range(1000)]

# Save the random integers to a file named "random_integers.txt"
with open("random_integers.txt", "w") as f:
    for integer in random_integers:
        f.write(str(integer) + "\n")

print("1000 random integers have been generated and saved to random_integers.txt")
