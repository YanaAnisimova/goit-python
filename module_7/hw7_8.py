def token_parser(s):
    if s == '':
        return []
    new_string = ''
    for i in s:
        if i == ' ':
            pass
        elif i in '*+-/':
            new_string += ' ' + i + ' '
        elif i == '(':
            new_string += i + ' '
        elif i == ')':
            new_string += ' ' + i
        else:
            new_string += i

    return new_string.split(' ')


print(token_parser('2+ 34 -5 * (3  + 9)/ 2'))
