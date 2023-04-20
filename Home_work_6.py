import string
import random

import time


def sum_of_list_items(nums):
    sum_nums = 0
    for num in nums:
        if type(num) == int:
            sum_nums += num
        elif type(num) == list:
            sum_nums += sum_of_list_items(num)

    return sum_nums


def cycle_abc(symbols, num):
    count = 0
    symbols_list = []
    for i in range(num):
        if count < len(symbols):
            i += 1
            symbols_list += symbols[count]
            count += 1
        else:
            count = 1
            symbols_list += symbols[0]
    return symbols_list


PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))


def attack():
    symbols = string.ascii_letters
    password = ''
    freeze_time = 0.1
    for i in range(4):
        for symbol in symbols:
            password += symbol

            if password_checker(password) < freeze_time:
                password = password[:-1]
            else:
                freeze_time += 0.1
                break

    return password


def password_checker(password):
    start = time.time()
    end = time.time()
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            break
        time.sleep(0.1)
        end = time.time()
    return end - start


if __name__ == "__main__":
    assert sum_of_list_items([1, 2, [4, 5], 25, [5, 6, 7]]) == 55
    assert cycle_abc(['a', 'b', 'c'], 7) == ['a', 'b', 'c', 'a', 'b', 'c', 'a']
    assert cycle_abc(['a', 'b', 'c'], 1) == ['a']
    assert cycle_abc(['a', 'b', 'c'], 0) == []
    assert attack() == PASSWORD
    # print("Real_Password: ", PASSWORD)
    # print("Passed_Password: ", attack())
