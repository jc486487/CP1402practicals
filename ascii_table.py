LOWER = 33
UPPER = 127

#accepts a charcater and prints its ASCII number
char= ord(input("Enter a character: "))
print("The ASCII code for {1} is {0}".format(char,chr(char)))

#accepts a number and prints its character
num = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while num<LOWER or num>UPPER:
    print("Incorrect range. Enter again")
    num = int(input(" "))
print("The character for {} is {}".format(num, chr(num)))

#prints the entire ASCII table
for i in range(LOWER, UPPER+1, 1):
    print("{} \t {}".format(i, chr(i)))
