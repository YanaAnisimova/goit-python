
import re

REG_PHONE = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

contact_list = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f'Command {e} not found!!!'
        except ValueError as e:
            return e
        except IndexError as e:
            return f'Command not full!!'
    return inner


def validate(reg, value):
    return re.search(reg, str(value))


def processing_com_hello():
    return 'How can I help you?'


def processing_com_exit():
    return 'Good bye!'


def processing_com_add(name, phone):
    if name in contact_list:
        raise ValueError(
            f'The new contact cannot be saved because the name [{name}] already exists. Please enter a different name.')
    if not validate(REG_PHONE, phone):
        raise ValueError(f'This phone number [{phone}] is not correct.')
    contact_list[name] = phone
    return f'New contact is saved: name [{name}], phone[{phone}]'


def processes_com_change(name, phone):
    if name not in contact_list:
        raise ValueError(
            f'Сontact with name [{name}] does not exist. Enter the correct name to update the contact\'s phone.')
    if not validate(REG_PHONE, phone):
        raise ValueError(f'This phone number [{phone}] is not correct.')
    contact_list[name] = phone

    return f'Saved a new phone number [{phone}] for a contact with the name [{name}].'


def processes_com_phone(name):
    return contact_list[name]


def processes_com_show_all():
    return contact_list


COMMAND = {'hello': processing_com_hello,
           'add': processing_com_add,
           'change': processes_com_change,
           'show all': processes_com_show_all,
           'phone': processes_com_phone,
           "exit": processing_com_exit
           }


@ input_error
def get_command_handler(user_input):
    if user_input[0] == "show" and user_input[1] == 'all':
        command = user_input[0] + " " + user_input[1]
        return COMMAND[command]()
    elif user_input[0] == "good" and user_input[1] == 'bye' or user_input[0] in ("close", "exit"):
        return COMMAND['exit']()
    elif user_input[0] == "phone" and user_input[1]:
        return COMMAND[user_input[0]](user_input[1])
    elif user_input[0] == "hello":
        return COMMAND[user_input[0]]()
    else:

        return COMMAND[user_input[0]](user_input[1], user_input[2])


def main():
    while True:
        user_input = input('Enter command: ').lower().split()
        result = get_command_handler(user_input)
        if result == 'Good bye!':
            print(result)
            break
        print(result)


if __name__ == '__main__':
    main()
