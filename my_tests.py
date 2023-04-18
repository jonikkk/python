import string
import random
import time


def attack(PASSWORD):
    symbols = string.ascii_letters
    password = ''
    for target_char in PASSWORD:
        for symbol in symbols:
            if symbol == target_char:
                password += symbol
                if password_checker(password, PASSWORD):
                    break
        else:
            password = password[:-1]
            continue
        if password == PASSWORD:
            return password
    return None


def password_checker(password, PASSWORD):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return False
        time.sleep(0.1)
    return True


PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))

