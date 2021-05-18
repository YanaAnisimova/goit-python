def get_emails(list_contacts):

    return list(map(lambda contact: contact['email'], list_contacts))
