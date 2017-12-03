class Credentials:
    """Create class for credentials"""

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        """Method that saves credential objects into credentials_list"""
        self.credentials_list.append(self)

    def delete_credential(self):
        """Method which deletes a particular credential"""
        Credentials.credentials_list.remove(self)

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

    @classmethod
    def credential_exists(cls, name):
        """Method to check whether a credential exists
        Args:
        name: name of account to search whether it exists
        boolean: True or False depending if the contatc exists
        """

        for credential in cls.credentials_list:
            if credential.account_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """Method which displays all current credentials"""
        return cls.credentials_list
