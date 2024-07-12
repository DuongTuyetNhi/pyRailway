class User:
    def __init__(self, username, password, pid=None):
        self.username = username
        self.password = password
        self.pid = pid

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_pid(self):
        return self.pid

