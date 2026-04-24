
# challenge 5 - count the vowels in a string

import os

def main():
    os.system("cls")
    enterString = input("Enter a string, and I'll count the vowels: ")
    print("For confirmation, your string is: ", enterString)

    vowelCount = 0
    for characters in enterString: 
        if characters.lower() in "aeiou": 
            vowelCount += 1
            
    print(f"The # of vowels in your string are: {vowelCount}")


if __name__ == "__main__":
    main()
