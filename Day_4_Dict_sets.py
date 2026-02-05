###TASK-3
friend_a={"Python","Cooking","Hiking","Movies"}
friend_b={"Hiking","Gaming","Photography","Python"}
print(friend_a & friend_b)

print(friend_a | friend_b)

print(friend_a - friend_b)


###TASK-2
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]


unique_users = set(raw_logs)

print("Is ID05 in unique_users?", "ID05" in unique_users)


print("Length of original list:", len(raw_logs))
print("Length of unique set:", len(unique_users))

####TASK 1
contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}


contacts["Diana"] = "444-444-4444"

contacts["Bob"] = "111-111-1111"


print("Alice's number:", contacts.get("Alice"))
print("Eve's number:", contacts.get("Eve", "Contact not found"))


for name, number in contacts.items():
    print(f"Contact: {name} | Phone: {number}")