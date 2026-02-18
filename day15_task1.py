import random
import itertools

# -------------------------------
# Customer Actions Probability
# -------------------------------

actions = ["Click", "Scroll", "Exit"]

# Generate Sample Space for two consecutive actions
sample_space = list(itertools.product(actions, repeat=2))

# Event E: At least one Click
event_E = [outcome for outcome in sample_space if "Click" in outcome]

probability_E = len(event_E) / len(sample_space)

print("Sample Space:", sample_space)
print("Total Outcomes:", len(sample_space))
print("Event E (At least one Click):", event_E)
print("Probability of clicking at least once:", probability_E)


# -------------------------------
# Dice Simulation (1000 Rolls)
# -------------------------------

trials = 1000
count_sum_7 = 0

for i in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    if dice1 + dice2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Experimental Probability of sum = 7:", experimental_probability)
