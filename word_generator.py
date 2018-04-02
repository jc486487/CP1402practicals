"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = str(input("Enter a word format\n(eg: ""ccvc*"", where c/%/* for consonants, v/#/* for vowels): "))
word = ""
for kind in word_format.lower():
    if kind in "c%*":
        word += random.choice(CONSONANTS)
    elif kind in "v#*":
        word += random.choice(VOWELS)

print(word)