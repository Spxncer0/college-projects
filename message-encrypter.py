# Started 16/10/23
message = input("Type something for it to be encrypted!:\n")


def encrypt(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "qwertyuiopasdfghjklzxcvbnm"

    result = ""
    for char in message:
        if char in alphabet:
            loc = alphabet.find(char)
            result += key[loc]
        else:
            result += char

    return result


result = encrypt(message)

print("encrypted text: " + result)
