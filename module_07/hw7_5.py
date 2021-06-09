def capital_text(s):

    new_string = []
    for i in s.split('.'):
        string_2 = []
        for j in i.split('!'):
            string_3 = []
            for k in j.split('?'):
                string_3.append(k.strip().capitalize())
            string_2.append('? '.join(string_3))
        new_string.append('! '.join(string_2))

    return '. '.join(new_string)


print(capital_text('alert. boss! oh'))
