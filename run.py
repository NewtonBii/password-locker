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
        print("Use these short codes to select an option: Create New User, cu, Login to your Account, lg")

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
                print(f"Congratulations {fname}. You can now create new accounts and store them")


if __name__ == '__main__':
    main()
