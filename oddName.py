"""Sherin Sarah Varghese """

name = str(input("Enter your name: "))
while name == "":
    print("Invalid. enter again")
    name = str(input("Enter your name: "))
new = ""

for i in range(0, len(name), 2):
    new += name[i] + ' '
print(new)
