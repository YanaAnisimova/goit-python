from collections import defaultdict


def group_clients(clients):

    grouped_id = defaultdict(list)

    for id in clients:
        grouped_id[id[:2]].append(id)

    return grouped_id


print(group_clients(['34345', '76788', '34654']))
