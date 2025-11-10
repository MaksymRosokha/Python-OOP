import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        combined = (self.username + password).encode("utf-8")
        return hashlib.sha256(combined).hexdigest()

    def check_password(self, password):
        return self._encrypt_password(password) == self.password

class PermissionError(Exception):
    pass

class AuthenticException(Exception):
    pass

class IncorrectPassword(AuthenticException):
    pass

class IncorrectUsername(AuthenticException):
    pass

class NotLoggedError(AuthenticException):
    pass

class PasswordTooShort(AuthenticException):
    pass

class UsernameAlreadyExists(AuthenticException):
    pass

class NotPermittedError(AuthenticException):
    pass



class Authenticator:
    def __init__(self):
        self.users = dict()

    def add_user(self, username, password):
        for user in self.users.values():
            if user.username == username:
                raise UsernameAlreadyExists("Username already exists")
        if len(password) <= 7:
            raise PasswordTooShort("The password is too short")
        self.users[username] = User(username, password)

    def login(self, username, password):
        if username not in self.users.keys():
            raise IncorrectUsername("Username is incorrect")
        if not self.users[username].check_password(password):
            raise IncorrectPassword("Password is incorrect")
        self.users[username].is_logged = True

    def is_logged_in(self, username):
        return self.users[username].is_logged

class Authorizor:
    def __init__(self, authenticator):
        self.permissions = dict()
        self.authenticator = authenticator

    def add_permission(self, permission):
        if permission in self.permissions.keys():
            raise PermissionError("Permission already exists")
        self.permissions[permission] = set()

    def permit_user(self, permission, username):
        if username not in self.authenticator.users.keys():
            raise IncorrectUsername("Incorrect username")
        if permission not in self.permissions.keys():
            raise PermissionError("Permission doesn't exist")
        self.permissions[permission].add(username)

    def check_permission(self, permission, username):
        if not username == None and not self.authenticator.is_logged_in(username):
            raise NotLoggedError("User isn't logged in")
        if permission not in self.permissions.keys():
            raise PermissionError("Permission doesn't exist")
        if username not in self.permissions[permission]:
            raise NotPermittedError("User doesn't have this permission")
        return True

authenticator = Authenticator()
authorizor = Authorizor(authenticator)