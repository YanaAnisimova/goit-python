import collections


def to_named(tup):

    Person = collections.namedtuple(
        'Person', ['id', 'surname', 'discount', 'city', 'age'])
    person = Person(tup[0], tup[1], tup[2], tup[3], tup[4])

    return person, tup[2]


print(to_named((1985, "Nick", 15, "Kharkiv", 34)))
