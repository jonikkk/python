import random


def retry(attempts=5, desired_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            print('Failure')

        return wrapper

    return decorator


@retry(desired_value=3)
def get_random_value_with_default_attempts():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


def copy_text(path_from, path_where):
    file_from = open(path_from)
    file_where = open(path_where, 'w')
    file_where.write(file_from.read())
    file_from.close()
    file_where.close()


def read_big_file(path):
    file = open(path)
    lines = 0
    size = 0
    chars = {}
    for line in file:
        lines += 1
        size += len(line)
        line = line.strip()
        for char in line:
            if char in ['\n', ' ']:
                continue
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    print({'lines = ': lines, 'Size = ': size,
           'Top_chars = ': (sorted(chars.items(), key=lambda item: item[1], reverse=True)[:3])})


if __name__ == '__main__':
    copy_text('text.txt', 'text_2.txt')
    read_big_file('text.txt')
    get_random_value()
    get_random_value_with_default_attempts()
    get_random_values_with_default_attempts([1, 2, 3, 4])
    get_random_values_with_default_attempts([1, 2, 3, 4], 2)
    get_random_values_with_default_attempts([1, 2, 3, 4], size=2)
    get_random_values_with_default_attempts(choices=[1, 2, 3, 4], size=2)
    get_random_values([1, 2, 3, 4])
    get_random_values([1, 2, 3, 4], 3)
    get_random_values([1, 2, 3, 4], size=1)
