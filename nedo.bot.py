def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Please try again."

    return wrapper

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

@input_error
def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        raise KeyError

@input_error
def get_phone(name):
    return f"The phone number for {name} is {contacts[name]}"

def show_all_contacts():
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts available"

def main():
    print("How can I help you?")
    while True:
        user_input = input("Enter your command: ").lower()
        if user_input.startswith("hello"):
            print("How can I help you?")
        elif user_input.startswith("add"):
            try:
                _, name, phone = user_input.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Invalid command. Please provide name and phone.")
        elif user_input.startswith("change"):
            try:
                _, name, phone = user_input.split()
                print(change_contact(name, phone))
            except ValueError:
                print("Invalid command. Please provide name and phone.")
        elif user_input.startswith("phone"):
            try:
                _, name = user_input.split()
                print(get_phone(name))
            except ValueError:
                print("Invalid command. Please provide name.")
        elif user_input.startswith("show all"):
            print(show_all_contacts())
        elif user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
