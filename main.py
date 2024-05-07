def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except Exception:
        return {}

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return f"Contact {name} added."
    except Exception as e:
        return f"Exception: {e}" 

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Contact {name} changed."
        else:
            return f"Contact {name} not found!"
    except Exception as e:
        return f"Exception: {e}"

def get_phone(args, contacts):
    try:
        if not args == []:            
            name = args[0]
            if name in contacts:
                phone = contacts.get(name)
                return phone
            else:
                return f"Contact {name} not found!"
        else:
                return f"Contact not found!"
    except Exception as e:
        return f"Exception: {e}" 

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
            print(f"Contacts: {contacts}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()