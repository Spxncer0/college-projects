# Started 16/10/2023

while True:
    word = input("Choose a word or a number, and it will be reversed: ")
    reversed_word = word[::-1]
    print(reversed_word)

    again = input("Would you like to input a new word or number? (y/n): ")
    while again != "y" and again != "n":
        print("Please enter either y or n")
        again = input("Would you like to input a new word or number? (y/n): ")

    if again == "n":
        print("Have a good day!")
        break
