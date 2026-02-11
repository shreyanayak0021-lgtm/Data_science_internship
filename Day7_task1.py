name=input("enter name:")
goal=input("Enter Your Daily Goal:")
with open("journal.txt","a") as file:
    file.write(f"name:{name},goal:{goal}\n")
            