import getpass

class User:
    user_db = {}

    def __init__(self, username, password):
        self.Username = username
        self.password = password
        self.voted = False

    @classmethod
    def add_user(cls, username, password):
        if username in cls.user_db:
            print("User already exists, try another.")
            return False
        cls.user_db[username] = User(username, password)
        return True

    @classmethod
    def authenticate(cls, username, password):
        user = cls.user_db.get(username)
        if user and user.password == password:
            return user  # Return the user object, not the User class
        return None

def Register():
    username = input("Enter a Username: ")
    password = getpass.getpass("Enter a Password: ")
    if User.add_user(username, password):
        print("\nUser registered successfully.\n")
    else:
        print("\nRegistration Failed.\n ")

def login():
    username = input("Enter a Username: ")
    password = getpass.getpass("Enter a Password: ")
    user = User.authenticate(username, password)  # Call User.authenticate instead of user.authenticate
    if user:
        print("Login Successful.")
    else:
        print("Invalid Username or Password.")
