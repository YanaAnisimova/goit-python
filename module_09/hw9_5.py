def format_phone_number(func):

    def inner(phone):

        if len(func(phone)) == 10:
            return '+38' + func(phone)
        elif len(func(phone)) == 12:
            return '+' + func(phone)

    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number("    +38(050)123-32-34"))
