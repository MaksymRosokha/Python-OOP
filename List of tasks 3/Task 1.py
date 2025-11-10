from authorization_system import *


class Editor:
    def __init__(self):
        self.username = None
        self.options = {"a": self.login, "b": self.test,
                        "c": self.change, "d": self.quit}

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            authenticator.add_user(username, password)
            authenticator.login(username, password)
            self.username = username
        except IncorrectUsername as e:
            print(e)
        except IncorrectPassword as e:
            print(e)

    def is_permitted(self, permission):
        try:
            if authorizor.check_permission(permission, self.username):
                return True
        except (NotLoggedError, PermissionError, NotPermittedError) as e:
            print(e)
        return False

    def test(self):
        if self.is_permitted("Testing"):
            print(f"{self.username} is testing")
        else:
            print(f"{self.username} isn't permitted for testing")

    def change(self):
        if self.is_permitted("Editing"):
            print(f"{self.username} is editing")
        else:
            print(f"{self.username} isn't permitted for editing")

    def quit(self):
        print("Goodbye")
        exit(0)

    def run(self):
        while True:
            for key, value in self.options.items():
                print(f"{key} - {value.__name__}")
            choice = input("Your choice: ")
            if choice not in self.options.keys():
                print("You entered incorrectly. Try again")
                continue
            self.options[choice]()


if __name__ == "__main__":
    users = {
        "Anna": "Password1",
        "Alex": "Password2",
        "Filip": "Password3"
    }
    for username, password in users.items():
        try:
            authenticator.add_user(username, password)
        except UsernameAlreadyExists as e:
            print(f"{username}: {e}")
        except PasswordTooShort as e:
            print(f"{username}: {e}")

        try:
            authenticator.login(username, password)
        except IncorrectUsername as e:
            print(f"{username}: {e}")
        except IncorrectPassword as e:
            print(f"{username}: {e}")

    try:
        authorizor.add_permission("Testing")
    except PermissionError as e:
        print(e)
    try:
        authorizor.add_permission("Editing")
    except PermissionError as e:
        print(e)
    try:
        authorizor.add_permission("Reading")
    except PermissionError as e:
        print(e)

    for username in users:
        try:
            authorizor.permit_user("Reading", username)
        except IncorrectUsername as e:
            print(e)
        except PermissionError as e:
            print(e)
    try:
        authorizor.permit_user("Editing", "Alex")
        authorizor.permit_user("Testing", "Anna")
    except IncorrectUsername as e:
        print(e)
    except PermissionError as e:
        print(e)

    editor = Editor()
    editor.run()
