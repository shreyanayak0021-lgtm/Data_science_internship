import random
P_heads = 1/2
P_six = 1/6
P_independent = P_heads * P_six

print("Probability of Heads AND rolling a 6 (Independent):", P_independent)

P_first_red = 5/10
P_second_red = 4/9

P_dependent = P_first_red * P_second_red

print("Probability of both marbles being Red (Dependent):", P_dependent)
trials = 10000
count_ind = 0

for i in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H" and die == 6:
        count_ind += 1

print("Experimental Probability (Independent):", count_ind / trials)

count_dep = 0

for i in range(trials):
    bag = ["R"]*5 + ["B"]*5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)

    if first == "R" and second == "R":
        count_dep += 1

print("Experimental Probability (Dependent):", count_dep / trials)
