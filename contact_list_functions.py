'''
addresses - list
phone numbers - list
emails - list
name - dictionary
age - dictionary
'''
def new_contact(contact_list):
    all_addresses = []
    all_phone = []
    all_email = []
    contact = {}
    contact['Name'] = input('Enter name: ')
    contact['Age'] = int(input('Enter age: '))

    address = input('Enter address: ')
    all_addresses.append(address)
    contact['Address(es)'] = all_addresses

    phone = input('Enter phone number: ')
    all_phone.append(phone)
    contact['Phone number(s)'] = all_phone

    email = input('Enter email: ')
    all_email.append(email)
    contact['Email(s)'] = all_email
    contact_list.append(contact)


def remove_contact(contact_list):
    view_contacts(contact_list)
    remove = int(input('Which contact would you like to delete: '))
    if 0 < remove <= len(contact_list):
     del contact_list[remove - 1]
     print('Contact deleted')
    else:
        print('Not valid')

def view_contacts(contact_list):
    if len(contact_list) == 0:
        print('No contacts :(')
    else:
        for i in range(len(contact_list)):
            print(i + 1, contact_list[i])
            