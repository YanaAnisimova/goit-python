def is_equal(utf_8_pass, utf_16_pass):

    decode_utf8 = utf_8_pass.decode('utf-8').casefold()
    decode_utf16 = utf_16_pass.decode('utf-16').casefold()

    return True if decode_utf8 == decode_utf16 else False
