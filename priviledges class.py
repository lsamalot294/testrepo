# Priviledges Class

# class: User as parent class

class User:
    def __init__(self, first_name, last_name, occupation, hobby):
        """defining a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        """describing the user's favorite things to do"""
        print(f"{self.first_name} works as a {self.occupation} and likes {self.hobby}")

    def greet_user(self):
        """hello to user"""
        print(f"Hello {self.first_name} {self.last_name}")

    def increment_login_info(self):
        """provide login number of attempts"""
        print(f"{self.first_name} has attempted to log-in {self.login_attempts} times")

    def increment_login_attempts(self, attempt):
        """to increment_login_attempts by 1"""
        self.login_attempts += attempt

    def reset_login_attempts(self):
        """resets login attempts to 0"""
        self.login_attempts = 0

class Priviledges:
    """A class that houses what priviledges are."""
    def __init__(self):
        """setting up the attributes of the class"""
        self.priviledges = ['can add post', 'can delete post', 'can ban user']

