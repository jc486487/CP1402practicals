words = []
word = str(input("Enter string: "))
while word != "":
    words.append(word)
    word = str(input("Enter string: "))

repeats = []
for x in range(0, len(words), 1):
    if words[x] in words[:x] and not repeats:
        repeats.append(words[x])

if len(repeats)>0:
    print("Strings repeated: ", " ".join(map(str, repeats)))
else:
    print("No repeated strings entered")