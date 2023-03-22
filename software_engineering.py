# Ryleigh Sperry

def print_menu():  # print menu function
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):  # create an encoding function that iterates through
    global new_password
    new_password = ""
    list(password)
    for i in password:
        i = int(i)
        i = (i + 3) % 10 #changed this so its only 1 digit after encoding
        i = str(i)
        new_password += i

    return new_password


def decode():
    print(f'The encoded password is {new_password} amd the original password is {password}')
    return


if __name__ == "__main__":
    program = True
    while program == True:
        option = int(input("Please enter an option:"))
        if option == 1:
            global password
            password = input("Please enter your password to encode:")
            new_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decode()
