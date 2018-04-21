count = 1
numbers = []
num = int(input("Number {}: ".format(count)))
while num >= 0:
    numbers.append(num)
    count += 1
    num = int(input("Number {}: ".format(count)))

smallest = min(numbers)
largest = max(numbers)
first = numbers[0]
last = numbers[-1]

average = sum(numbers)/len(numbers)

print("The first number is {0} \nThe last number is {1} \nThe smallest number is {2} \nThe largest number is {3} \nThe average of the numbers is {4}".format(first, last, smallest, largest, average))