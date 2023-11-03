# Lisy's code (+ Daniel's Decode)

def print_menu():
    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")


def encode_number(password):
    encoded_pass = ""
    for digit in password:
        if digit.isdigit():
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_pass += encoded_digit
        else:
            encoded_pass += digit
    return encoded_pass


def decode_number(password):
    decoded_pass = ""
    return decoded_pass


if __name__ == '__main__':
    while True:
        print_menu()
        menu_option = input(f"Please enter an option: ")
        if menu_option == "1":
            password = input(f"Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif menu_option == "2":
            if password is not None:
                encoded_password = encode_number(password)
                print(f"The encoded password is {encoded_password}, and the original password is {password}")
            else:
                print(f"No password has been encoded yet.")
        elif menu_option == "3":
            break
        else:
            print(f"Invalid option. Please enter 1, 2, or 3 to choose from the menu.")
