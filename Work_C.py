class Person:
    def __init__(self, first_name, surname, personal_code):
        self.first_name = first_name
        self.surname = surname
        self.personal_code = personal_code
    
    def __str__(self):
        return f"Name: {self.first_name} {self.surname}, Personal Code: {self.personal_code}"


persons_dict = {}


def add_person():
    first_name = input("Enter first name: ").strip()
    surname = input("Enter surname: ").strip()
    personal_code = input("Enter personal code: ").strip()
    
    if personal_code in persons_dict:
        print(f"Person with personal code {personal_code} already exists!")
    else:
        persons_dict[personal_code] = Person(first_name, surname, personal_code)
        print("Person added successfully!")


def remove_by_personal_code():
    personal_code = input("Enter personal code to remove: ").strip()
    
    if personal_code in persons_dict:
        removed_person = persons_dict.pop(personal_code)
        print(f"Removed: {removed_person}")
    else:
        print("Person with this personal code not found!")


def remove_by_name():
    first_name = input("Enter first name: ").strip()
    surname = input("Enter surname: ").strip()
    
    found_code = None
    for code, person in persons_dict.items():
        if person.first_name.lower() == first_name.lower() and person.surname.lower() == surname.lower():
            found_code = code
            break
    
    if found_code:
        removed_person = persons_dict.pop(found_code)
        print(f"Removed: {removed_person}")
    else:
        print("Person with this name not found!")


def search_by_name():
    """Search by first name and display the last found person's surname"""
    first_name = input("Enter first name to search: ").strip()
    
    matching_persons = []
    for person in persons_dict.values():
        if person.first_name.lower() == first_name.lower():
            matching_persons.append(person)
    
    if matching_persons:
        last_person = matching_persons[-1]
        print(f"Last person found with name '{first_name}': {last_person.surname}")
    else:
        print(f"No person found with first name '{first_name}'!")


def display_all_persons():
    if not persons_dict:
        print("No persons in the database!")
    else:
        print("\n--- All Persons ---")
        for person in persons_dict.values():
            print(person)
        print("-------------------")

def main():
    while True:
        print("\n=== Person Storage System ===")
        print("1. Add person")
        print("2. Remove person by personal code")
        print("3. Remove person by first and last name")
        print("4. Search by name (displays last person's surname)")
        print("5. Display all persons")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_person()
        elif choice == '2':
            remove_by_personal_code()
        elif choice == '3':
            remove_by_name()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            display_all_persons()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()