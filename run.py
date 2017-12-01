#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credentials


def create_user(fname, lname, email, user_password):
    """Function to create a new user"""
    new_user = User(fname, lname, email, password)
    return new_user


def save_new_user(user):
    """Function to save the new user"""
    user.save_user()


def create_new_credential(account_name, _account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()


def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name()


def display_credentials():
    """Function which displays all saved credentials"""
    return Credentials.display_credentials()


def main():
    print("Welcome to PassWord Locker.")
    print('\n')
    print("Use these short codes to select an option: Create New User use 'cu': Login to your account use 'lg' or 'ex' to exit password locker")

    while True:
        short_code = input().lower()

        if short_code == 'cu':
            print("First Name")
            fname = input()

            print("Last name")
            lname = input()

            print("Your Email")
            email = input()

            print("Enter a password")
            user_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            if confirm_password != user_password:
                print("Sorry your passwords did not match")
                print("Enter a password")
                user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {fname} {lname}! You have created your new account.")
                print('\n')

        elif short_code = 'lg':
            print("WELCOME")
            print("Enter Your UserName")

                print("Please select an option to continue: Use either 1, 2, 3, 4 or 5 to select an option")
                print("1: View Your saved credentials")
                print("2: Add new credentials")
                print("3: Remove credentials")
                print("4: Search credentials")
                print("5: Log Out")
                option = input()

                if option == '2':
                    print("Enter The Account Name")
                    account_name = input()
                    print("Enter a password")
                    print("To generate random password enter keyword 'gp' or 'n' to create your own password")
                    keyword = input().lower()
                    if keyword == 'gp':
                        account_password = random.randint(111111, 1111111)
                        print(f"Your password is: {account_password}")
                        print('\n')
                    elif keyword == 'n':
                        print("Create your password")
                        account_password = input()
                        print(f"Your password is: {account_password}")
                        save_new_credential(create_new_credential(account_name, account_password))

                    else:
                        print("Please enter a valid Code")

                elif option == '1':
                    if display_credentials():
                        print("Below is a list of all your credentials")

                        for credential in display_credentials():
                            print(f"ACCOUNT NAME:{credential.account_name}")
                            print(f"PASSWORD:{credential.account_password}")
                            print('\n')

                    else:
                        print('\n')
                        print("You don't seem to have any contacts yet")
                        print('\n')
                    # while True:
                # else:
                #     print("Sorry you did not select a valid code")
                elif option == '5':
                    print("You have Successfully logged out")

                elif option == '3':
                    print("It works")

                else:
                    print("Please enter a valid code")

        # elif short_code == 'ex':
        #     print("Bye....")
        #     break
    else:
        print("Please Enter a valid code to continue")
        #


if __name__ == '__main__':
    main()
