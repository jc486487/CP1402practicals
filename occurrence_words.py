sentence = str(input("Enter a sentence: ")).split()
sentence.sort()
count = {}
for word in sentence:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for key, value in count.items():
    print("{} : {}".format(key,value))