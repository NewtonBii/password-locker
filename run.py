#!/usr/bin/env python3.6
from user import User


def create_user(fname, lname, email, password):
    """Function to create a new user"""
    new_user = User(fname, lname, email, password)
    return new_user


def save_new_user(user):
    """Function to save the new user"""
    user.save_user()


def main():
    print("Welcome to PassWord Locker.")
    print('\n')
    while True:
        print("Use these short codes to select an option: Create New User, cu, Exit Password Locker, ex")

        short_code = input().lower()

        if short_code == 'cu':
            print("First Name")
            fname = input()

            print("Last name")
            lname = input()

            print("Your Email")
            email = input()

            print("Enter a password")
            password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while(confirm_password != password):
                print("Sorry your passwords did not match")
                print("Enter a password")
                password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {fname} {lname}! You have created your new account.")
                print("Please select an option to continue")
                print("1: View Your saved credentials")
                print("2: Add new credentials")
                print("3: Remove credentials")
                print("4: Search credentials")
                print("5: Exit Password Locker")

                option = input()
                # while True:
                # else:
                #     print("Sorry you did not select a valid code")
        elif short_code == 'ex':
            break


if __name__ == '__main__':
    main()
