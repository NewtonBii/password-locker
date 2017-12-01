import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """Test class that defines test cases for the Credentials class behavior
    """

    def setUp(self):
        """Set up method to run befor before each test case"""
        self.new_credentials = Credentials("Facebook", "12345")

    def test_credentials_instance(self):
        """Method that tests whether the new_credentials have been instantiated correctly"""
        self.assertEqual(self.new_credentials.account_name, "Facebook")
        self.assertEqual(self.new_credentials.account_password, "12345")

    def test_save_credentials(self):
        """Method that tests whether the new credential created has been saved"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """Method that saves multiple credentials to credentials_list"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Twitter", "56789")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        """Method that clears the credentials_list after every test to ensure that there is no error"""
        Credentials.credentials_list = []


if __name__ == '__main__':
    unittest.main()
