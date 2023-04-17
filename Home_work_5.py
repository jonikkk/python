STRING = 'Hello_world!'

print(STRING[::-1])

STRING_LENGHT = len(STRING)
assert STRING_LENGHT == 12

string_list = list(STRING)
print(string_list)

STRING_CHOICE = str('|'.join(string_list[2::3]))
print(STRING_CHOICE)


def count_chars_v1(s1):
    if s1 == '':
        return {}
    else:
        char_dict = count_chars_v1(s1[1:])
        if s1[0] in char_dict:
            char_dict[s1[0]] += 1
        else:
            char_dict[s1[0]] = 1
        return char_dict


def count_chars_v2(s1):
    if s1 == '':
        return {}
    else:
        char_dict = count_chars_v2(s1[1:])
        char_dict[s1[0]] = s1.count(s1[0])
        return char_dict


def max_length(list_1):
    long_string = ''
    for abc in list_1:
        if len(abc) > len(long_string):
            long_string = abc
    return long_string


def divide_and_glue(string, delim):
    words = string.split(delim)
    words.sort()
    return delim.join(words)


def print_string(list_2):
    string = ''
    for number in list_2:
        string += chr(number)
    return string


if __name__ == '__main__':
    list1 = ['kjs/d%bh/fk$$$js%dhf/GHHGHF', 'kfjghlfgkhj]', 'fghf', 'qweqwewqewqewqewqew']
    STRING = str(list1[0])
    list2 = [119, 101, 108, 108, 32, 100, 111, 110, 101]
    print(count_chars_v1('Hello_world!'))
    print(count_chars_v2('Hello_world!'))
    print(max_length(list1))
    print(divide_and_glue(STRING, "/"))
    print(print_string(list2))
