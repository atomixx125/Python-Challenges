#challenge 4 - implement [::-1]

# string = "hello"
# accumulateString = ""

# for strings in range(len(string)-1, -1,-1):
#     accumulateString += string[strings]
# print(accumulateString)

userString = input("Enter a string to reverse manually: ")

accumulateString = ""

for x in range(len(userString) -1 , -1, -1): 
    accumulateString += userString[x]

print(accumulateString)