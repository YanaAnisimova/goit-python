def is_integer(s):

    s = s.strip().removeprefix('+').removeprefix('-'))

    return True if s.isdigit() and len(s) >= 1 else False
