# Ryleigh Sperry

def print_menu(): #print menu function
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password): # create an encoding function that iterates through 
    new_password = ""
    list(password)
    for i in password:
        i = int(i)
        i += 3
        i = str(i)
        new_password += i


    return new_password






if __name__ == "__main__":
    program = True
    while program == True:
        option = int(input("Please enter an option:"))
        if option == 1:
            password = input("Please enter your password to encode:")
            password = encode(password)
            print("Your password has been encoded and stored!")





