import unittest
from password_locker_test import Account


class TestAccount(object):
    """Test class that defines test cases for the account class behaviour"""

    def setUp(self):
        """Set Up Method to run before each test case to check if the class has been instantiated correctly"""
        self.new_account = Account("NewUser", "12345")
