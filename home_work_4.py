def get_position_args(*args):
    return print(set(args))


def set_named_args(**kwargs):
    print(len(kwargs))
    if len(kwargs['user_type']) > 0:
        return kwargs
    else:
        kwargs['user_type'] = 'Student'
        return kwargs


get_position_args(4, 5, 7, 4, 8, 'hi', 'hi', 'lib', (5, 6), (5, 6))

print(set_named_args(user_type='Student', name='Eugene',
                     last_name='Yevtushenko', age=36, tel='3123123123'))
print(set_named_args(user_type='Employer', user='eugene'))


def multi_args(arg_pos_1, arg_pos_2, /, arg_multy, *, arg_named_1,
               arg_named_2='Empty', arg_named_3='Full'):
    pass


def func_a(num1):
    def func_inside(num2):
        return num1 + num2

    return func_inside


func_b = func_a(5)
assert func_b(4) == 9
assert func_b(15) == 20
assert func_b(7) == 12


def draw_square(lenght):
    def draw_star(weight):
        if weight == 0:
            return 0

        else:
            print('*  ' * lenght)

        return draw_star(weight - 1)

    return draw_star


SQUARE_SIZE = 10
draw = draw_square(SQUARE_SIZE)
draw(SQUARE_SIZE)
