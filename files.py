#program 1
name_file = open("name.txt", 'w')
name = str(input("Enter your name: "))
print(name, file=name_file)
name_file.close()

#program 2
in_file= open("name.txt", 'r')
name= in_file.read().strip()
print("Your name is ",name)
in_file.close()

#program 3
out_file= open("numbers.txt", 'r')
number_1= int(out_file.readline())
number_2= int(out_file.readline())
print(number_1 + number_2)
out_file.close()

#program 4
numbers_file= open("numbers.txt", 'r')
sum = 0
for i in numbers_file:
    sum += int(i)
print("Result: ",sum)
numbers_file.close()
