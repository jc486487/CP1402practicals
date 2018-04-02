import random
print(random.randint(5, 20)) # line 1
print(random.randrange(3, 10, 2)) # line 2
print(random.uniform(2.5, 5.5)) #line 3

#What did you see on line 1?
#random integer gets printed between the range 5 & 20

#What was the smallest number you could have seen, what was the largest?
#smallest: 5; largest: 20

#What did you see on line 2?
#prints a random element according to the range description; here it will be an odd number between 3 & 10

#What was the smallest number you could have seen, what was the largest?
#smallest: 3; largest: 10

#Could line 2 have produced a 4?
#no it wouldn't as the step value is 2

# What did you see on line 3?
#a random floating point number is generated. Here the difference is that the stop value can also get printed.

#What was the smallest number you could have seen, what was the largest?
#smallest: 2.5; largest: 5.5