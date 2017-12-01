import unittest
from account import Account


class TestAccount(unittest.TestCase):
    """Test class that defines test cases for the account class behaviour"""

    def setUp(self):
        """Set Up Method to run before each test case to check if the class has been instantiated correctly"""
        self.new_account = Account("NewUser", "12345")

    def test_init(self):
        """Test to ensure that the object is initialized properly"""
        self.assertEqual(self.new_account.account_name, "NewUser")
        self.assertEqual(self.new_account.password, "12345")

    def test_save_account(self):
        """Method that tests wether an account credentials have been successfully saved"""
        self.new_account.save_account()
        self.assertEqual(len(Account.account_list), 1)


if __name__ == '__main__':
    unittest.main()
