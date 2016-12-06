Pseudocode
for l in word:
    if l not in v:
        message += l


Implementation 
v = ("a", "e", "i", "o", "u")

word = input("Please enter the word you want remove the vowels : ")

message = ""

for l in word:
    if l in v:
        message += l

print (message)
