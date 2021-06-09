from collections import deque


def form_deque(clients_id, max_len):

    d = deque(maxlen=max_len)
    count = 0
    while clients_id[count] % 2:
        count += 1
        continue
    for id in clients_id[count:]:
        d.append(id)
    for id in clients_id[:count]:
        d.append(id)
    return d


print(form_deque([1233, 4566, 1234, 7877, 2], 5))
