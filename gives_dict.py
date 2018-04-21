names = []
age = []
for x in range(1, 6, 1):
    name = str(input("Enter name: "))
    num = int(input("Enter age: "))
    names.append(name)
    age.append(num)
#print(names)
#print(age)
print(dict(zip(names,age)))
