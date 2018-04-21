C_CODES= {"aliceblue": "#f0f8ff", "brown": "#a52a2a", "blueviolet": "#8a2be2", "blue": "#0000ff", "black": "#000000",
          "beige": "#f5f5dc", "chocolate": "#d2691e", "deepskyblue": "#00688b", "floralwhite": "#fffaf0",
          "firebrick": "#8b1a1a"}

name = str(input("Enter a colour name: ")).lower()
while name not in C_CODES:
    print("Invalid short state")
    name = str(input("Enter a colour name: ")).lower()
print(name, "is", C_CODES[name])