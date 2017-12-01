class Credentials:
    """Create class for credentials"""

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        """Method that saves credential objects into credentials_list"""
        self.credentials_list.append(self)

    @classmethod
    def find_by_name(cls, account_name):
        """Method that takes in a name and returns a credential that matches that particular name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and it's corresponding PassWord
        """

        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential
