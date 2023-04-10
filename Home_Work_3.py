def func_find_max(num1, num2):
    return num1 if num1 > num2 else num2


print(func_find_max(7, 9))


def func_find_min(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1

    return num2 if num2 <= num3 else num3


print(func_find_min(500, 6, 120))


def func_module(num):
    return num if num > 0 else -num


print(func_module(-56))


def func_addition(num1, num2):
    return num1 + num2


print(func_addition(4, 5))


def func_check(num):
    if num == 0:
        return print('Equal Zero')
    if num > 0:
        return print('Positive')
    else:
        print('Negative')


func_check(5)
