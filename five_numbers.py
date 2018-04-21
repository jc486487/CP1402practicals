numbers = []
for x in range(0, 5, 1):
    number = int(input("Number: "))
    numbers.append(number)
    
smallest = min(numbers)
largest = max(numbers)
first = numbers[0]
last = numbers[-1]

average = sum(numbers)/len(numbers)

print("The first number is {0} \nThe last number is {1} \nThe smallest number is {2} \nThe largest number is {3} \nThe average of the numbers is {4}".format(first, last, smallest, largest, average))