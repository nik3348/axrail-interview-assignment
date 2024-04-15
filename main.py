def dispense_change(amount):
    notes = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}
    for note, value in notes.items():
        while amount >= note:
            amount -= note
            value += 1
            notes[note] = value
    return notes


def vending_machine():
    drinks = {
        "A1": {"name": "Coke", "price": 3},
        "B2": {"name": "Sprite", "price": 5},
        "C3": {"name": "100 Plus", "price": 2},
        "D4": {"name": "Water", "price": 1},
    }

    print("Available drinks:")
    for code, drink in drinks.items():
        print(f"{code}: {drink['name']} (RM{drink['price']})")

    choice = input("Enter drink code: ").upper()
    if choice not in drinks:
        print("Invalid choice. Please try again.")

    selected_drink = drinks[choice]
    print(f"\nYou chose {selected_drink['name']} (RM{selected_drink['price']}).")

    payment = 0
    while payment < selected_drink["price"]:
        cash = int(input("Insert amount (whole notes only): "))
        if cash not in [1, 5, 10, 20, 50, 100]:
            print("Invalid note. Please insert whole notes only.")
            continue        
        payment += cash

    if payment < selected_drink["price"]:
        print("Insufficient amount. Please insert more money.")

    change = payment - selected_drink["price"]
    if change > 0:
        print(f"\nDispensing your {selected_drink['name']}.")
        change_details = dispense_change(change)
        print("Change:")
        for note, count in change_details.items():
            if count > 0:
                print(f"{count} x RM{note} notes")


if __name__ == "__main__":
    vending_machine()
