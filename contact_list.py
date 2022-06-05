import contact_list_functions
import sys
def main():
    contact_list = []
    while True:
        choice = int(input('(1)Add a contact\n'
                           '(2)Remove a contact\n'
                           '(3)View contacts\n'
                           '(4)Exit\n'
                           'What would you like to do?\n'))
        if choice == 4:
            sys.exit(0)
        if choice == 1:
            contact_list_functions.new_contact(contact_list)
        if choice == 2:
            contact_list_functions.remove_contact(contact_list)
        if choice == 3:
            contact_list_functions.view_contacts(contact_list)

main()
