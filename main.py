def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"

    return inner

def parse_input(user_input):
    # try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    # except Exception:
        # return {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} changed."
    else:
        return f"Contact {name} not found!"

@input_error
def get_phone(args, contacts):
    if not args == []:
        name = args[0]
        if name in contacts:
            return contacts.get(name)
    else:
        return f"Contact not found!"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
                
        
        if not user_input or user_input.strip() == "": # Check for empty input
            command = ""
        else:  
            command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            # print(show_contacts(contacts))
            for key, value in contacts.items():
                print(f'{key}: {value}')
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()