import random


class Password_manager:

    CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', "n", 'o',
                  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    SPECIAL = ['*', '&', '-', '.', '@', '_', '<', '>', '%', '!']
    SUGGESTED_PASSWORD = ""
    MINIMUM_LENGTH = 10

    def __init__(self, *args):
        """
        first = length of password
        second = Minimum length
        :param args:
        """
        try:
            if args[0] >= self.MINIMUM_LENGTH:
                self.length_of_password = args[0]
            else:
                difference = self.MINIMUM_LENGTH - args[0]
                self.length_of_password = args[0] + difference

        except:
            self.length_of_password = self.MINIMUM_LENGTH

    def create_password(self):

        for chars in range(self.length_of_password):
            self.SUGGESTED_PASSWORD += random.choice(self.CHARACTERS)
            self.SUGGESTED_PASSWORD += str(random.choice(self.NUMBERS))
            self.SUGGESTED_PASSWORD += random.choice(self.SPECIAL)
            self.SUGGESTED_PASSWORD += (random.choice(self.CHARACTERS)).upper()
        return self.remove_extra_elem()

    def remove_extra_elem(self):

        _password = list()
        for i in range(self.length_of_password):
            _password.append(self.SUGGESTED_PASSWORD[i])
        self.SUGGESTED_PASSWORD = ''.join(map(str, _password))
        del _password
        return self.SUGGESTED_PASSWORD

password = Password_manager(13)
pass_word = password.create_password()
print('Return password :: ', pass_word)
