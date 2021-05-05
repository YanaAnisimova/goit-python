def sequence_buttons(string):
    string = string.casefold()
    LETTERS = '.,?!:abcdefghijklmnopqrstuvwxyz '
    NUMBERS = ('1', '11', '111', '1111', '11111', '2', '22', '222', '3', '33', '333', '4', '44', '444', '5',
               '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999', '0')
    TRANSLIT_DICT = {}

    for l, n in zip(LETTERS, NUMBERS):
        TRANSLIT_DICT[ord(l)] = n

    return string.translate(TRANSLIT_DICT)


print(sequence_buttons('Hi there!'))
