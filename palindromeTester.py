# Started 16/10/23

while True:
    word = input("Type a word/number and see if it palindrome!: ")
    reversed_word = word[::-1]  # This reverses the user input
    if reversed_word == word:  # This checks if the word is a palindrome
        print("The word/number is a palindrome!")
    if reversed_word != word:
        print("The word/number is NOT a palindrome!")

    again = input("Would you like to input a new word/number? (y/n): ")
    while again != "y" and again != "n":
        print("Please enter either y or n...")
        again = input("Would you like to input a new word/number? (y/n): ")

    if again == "n":
        print("Have a good day!")
        break
