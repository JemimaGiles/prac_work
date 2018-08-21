MIN_LENGTH = 6


def main():
    password = get_password()

    print_password(password)


def print_password(password):
    for char in password:
        print("*", end='')


def get_password():
    password = input("enter password: ")
    while len(password) < MIN_LENGTH:
        print("password too short")
        password = input("enter password: ")
    return password


main()
