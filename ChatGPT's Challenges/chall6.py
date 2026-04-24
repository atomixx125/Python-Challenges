
# challenge 6 - check if a number is prime

userInput = int(input("Enter a number: "))

print(f'you inputted: {userInput}')


if userInput <= 1: 
    print("not prime")

elif userInput == 2:
    print("prime!")
else: 
    primeCheck = True
    for nums in range(2, userInput):
        if userInput % nums == 0: 
            primeCheck = False
            break
    if primeCheck:
        print("prime!")
    else:
        print("not prime!")





# if userInput % userInput == 0 and userInput % 1 == 0:
#     print("prime!")
# elif userInput == 1 or userInput == 2: 
#     print("prime!")
# else:
#     print("not prime!")


# if userInput % 2 == 0: 

#     print('not prime!')