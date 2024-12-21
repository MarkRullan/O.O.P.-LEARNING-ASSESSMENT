#O.E. #2
#Mark J. Rullan

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        
def __str__(self):

        return f"{self.brand} {self.model} - P{self.price}"
    
def update(self, brand='', model='', price=None):
    if brand != '': 
        self.brand = brand
    if model != '':
        self.model = model
    if price != '': 
        self.price = price
        
def add_phone(phones):
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = float(input("Enter phone price: "))
    phone = Phone(brand, model, price)
    phones.append(phone)
    print("Phone added successfully!")
    
def modify_phone(phones):
    list_phones(phones)

    phone_index = input("Enter the index of the phone to modify: ")

    if phone_index.isdigit():
        phone_index = int(phone_index)

        if 0 <= phone_index < len(phones):
            phone = phones[phone_index]
            print(f"Selected Phone: {phone}")

            brand = input("Enter new brand (leave blank to keep current): ")
            model = input("Enter new model (leave blank to keep current): ")
            price_input = input("Enter new price (leave blank to keep current): ")

            price = float(price_input) if price_input else None

            phone.update(brand, model, price)

            print("Phone updated successfully!")
        else:
            print("Invalid phone index. Please select a valid index from the list.")
    else:
        print("Invalid input. Please enter a number for the index.")
        
def delete_phone(phones):
    list_phones(phones)

    phone_index = input("Enter the index of the phone to delete: ")

    if phone_index.isdigit():
        phone_index = int(phone_index)

        if 0 <= phone_index < len(phones):
            del phones[phone_index]
            print("Phone deleted successfully!")
        else:
            print("Invalid phone index. Please select a valid index from the list.")
    else:
        print("Invalid input. Please enter a number for the index.")   
        
def list_phones(phones):
    """Lists all the phones in the collection."""
    if phones:
        print("\nList of Phones:")
        index = 0
        for phone in phones:
            print(f"{index}. {phone}")
            index += 1 
    else:
        print("No phones available.")     

def main():
    phones = []

    while True:
        print("\n--- Phone Management System ---")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. List Phones")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_phone(phones)
        elif choice == '2':
            modify_phone(phones)
        elif choice == '3':
            delete_phone(phones)
        elif choice == '4':
            list_phones(phones)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose between 1 and 5.")

if __name__ == "__main__":
    main()
