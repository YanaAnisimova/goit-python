# This code is working in VS, but in autocheck not.

# def encode(data):

#     if data == [] or data == '':
#         return []

#     elif data[1] == data[0]:
#         count = 1
#         while count < len(data) and data[count] == data[0]:
#             count += 1
#         quantity = [count]

#         return list(data[0:1]) + quantity + encode(data[count:])


def encode(data, final_data=False):
    if not final_data:
        final_data = []
    if data == [] or data == '':
        return final_data
    else:
        if len(final_data) > 1 and final_data[-2] == data[0]:
            final_data[-1] += 1
        else:
            final_data.append(data[0])
            final_data.append(1)
        return encode(data[1:], final_data)


print(encode(['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']))
print(encode("XXXZZXXYYYZZ"))
