###TASK -1
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final inventory:", inventory)

##TASK2
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First reading (index 0):", temperatures[0])
print("Last reading (index -1):", temperatures[-1])
afternoon_peak = temperatures[3:6]
print("Afternoon Peak readings (index 3:6):", afternoon_peak)
last_three = temperatures[-3:]
print("Last 3 Hours readings (index -3:):", last_three)

###TASK3
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
print("Tuples cannot be modified!")