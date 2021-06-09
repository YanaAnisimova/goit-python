def get_favorites(contacts):

    return list(filter(lambda x: bool(x["favorite"]), contacts))


print(get_favorites([{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}, {
    "name": "Vov Vov",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": True,
}]))
