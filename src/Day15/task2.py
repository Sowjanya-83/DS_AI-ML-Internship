import random

trials = 100000
count_independent = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)
    if coin == "H" and die == 6:
        count_independent += 1

prob_independent = count_independent / trials

print("Independent Event:")
print("Experimental Probability (Heads AND 6):", prob_independent)
print("Theoretical Probability:", 1/12)

count_dependent = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)
    if first == "R" and second == "R":
        count_dependent += 1

prob_dependent = count_dependent / trials

print("\nDependent Event:")
print("Experimental Probability (Both Red):", prob_dependent)
print("Theoretical Probability:", 2/9)
