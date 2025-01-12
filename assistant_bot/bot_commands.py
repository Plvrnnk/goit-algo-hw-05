def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return 'Name does not exist! Try again please.'
        except IndexError:
            return 'Enter the argument for the command. Try again please'
    return inner

# @input_error
def hello():
    return 'How can I help you?'

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact changed'

@input_error 
def show_phone(args, contacts):
    name = args[0]
    return f"{name}'s phone is {contacts[name]}"

# @input_error 
def show_all(contacts):
    return 'Contacts:', contacts

# @input_error
def command_list():
    return 'List of commands:\n1.hello\n2.add (username) (phone)\n3.change (username) (phone)\n4.phone (username)\n5.all\n6.commands\n7.close or exit'