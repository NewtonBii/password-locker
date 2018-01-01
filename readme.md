# PASSWORD LOCKER

This project was generated with ```Python3.6.```

## Installation

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Run ```python3.6 run.py``` code in the terminal to launch.

# Usage

* Once you launch, You can either create a new user, or login or exit the application.
* If you choose to ```login(lg),``` use: ```testuser``` as username and ```12345``` as PassWord
* If you choose to create a new account, use ```cu``` as the code and follow the prompts.
* Once logged in, you can:
```
     1: View Your saved credentials.
     2: Add new credentials.
     3: Remove credentials.
     4: Search credentials.
     5: Log Out.
```
## Running unit tests

* Run ```python3.6 credentials_test.py``` for credential class tests.
* Run ```python3.6 test_user.py``` for user class tests.

# Bugs.

Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session.
You can still use the default login but if you exit the app, you will still loose all the credentials you created.

## Further help
For additions, submit a pull request and once approved you can make contributions at will.
Alternatively contact me at: ```biinewton382@gmail.com```

# License

MIT License.
