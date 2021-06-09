import collections


def count_activity(clients_activity):

    common_list = []
    for list in clients_activity:
        for name in list:
            common_list.append(name)
    activity_counts = collections.Counter(common_list)

    print(activity_counts)
    most_active = activity_counts.most_common(1)
    return most_active


print(count_activity([['Edvardson', 'Damriel', 'Mbape',
                       'Columb'], ['Edvardson', 'Mbape', 'Mbape']]))
