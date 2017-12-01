class User:
    """Create class for users"""

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    user_list = []

    def save_user(self):
        """Method that saves user objects into user_list"""
        self.user_list.append(self)


if __name__ == '__main__':
    main()
