data = {}
for x in range(1, 6, 1):
    name = str(input("Enter name: "))
    birth = str(input("Enter age (dd/mm/yyyy): "))
    data[name] = birth

#new_data = {}
for y in data.values():
    print(y.split())

year = int(y[2])
    age = 2018 - year
    new_data[name] = age

print(new_data)