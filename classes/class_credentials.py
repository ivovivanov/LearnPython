from random_string import generate_rand_string as passgen
import re

class credentials():
    id = 0
    def __init__(self, username):
        credentials.id += 1
        self.__id = credentials.id
        self.__username = username
        self.__password = None
        self.__email = None
        print('New user credential created for user id {} with username {}!'.format(credentials.id, self.username))
        
    @property
    def username(self):
            return self.__username

    @username.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Username should be string value")
        self.__username = value

    @property
    def password(self):
        if self.__password is None:
            return 'not set'
        else:
            return (len(self.__password) * '*')

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password should be string value")
        self.__password = value
    
    @property
    def email(self):
        if self.__email is None:
            return 'not set'
        else:
            return (self.__email)

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("Password should be string value")
        elif validate_email(email):
            self.__email = email
        else:
            self.__email = None


    def change_password(self, password = 'generate'):
        if password == 'generate':
            self.password = passgen()

    def __str__(self):
        return 'Credentials information:\nid: {}\n username: {}\n email: {}\n password: {}\n' \
            .format(self.__id, self.username,  self.email, self.password)        


def validate_email(email: str) -> bool:
    check=re.search('^(\w+[.|\w])*@(\w{2,}[.])+\w{2,}$', email)
    return True if check is not None else False


if __name__ == '__main__':
    ivo_credentials = credentials('ivoivanov')
    print()
    print(ivo_credentials)
    ivo_credentials.change_password()
    print(ivo_credentials)
    ivo_credentials.email = 'thisisnotvalid'
    print(ivo_credentials)
    elena = credentials('elena1993')
    print(elena)
    print(ivo_credentials)
    
