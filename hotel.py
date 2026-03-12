room_numbers_list = list(range(1, 101))
room_types = ["standard", "luxury"]
guests = [
    {"Name": "Asadbek", "Room number": 1, "Room type": "standard"},
    {"Name": "Sabina", "Room number": 12, "Room type": "deluxe"},
]


def add_guest():
    pass


def delete_guest():
    pass


def guests_list():
    # The <15 means "allocate 15 spaces, left-aligned"
    print(f"{'NAME':<15} | {'ROOM #':<10} | {'TYPE'}")
    print("-" * 40)
    for guest in guests:
        print(
            f"{guest['Name']:<15} | {guest['Room number']:<10} | {guest['Room type']}"
        )


def show_menu():
    print("*" * 40)
    print("Welcome to the Homodiv's hotel !!!")
    print("*" * 40)
    print("\n" + "*" * 40)
    print("1 - add guest\n2 - delete guest\n3 - guests list\n0 - exit")
    print("*" * 40)


def main():
    while True:
        show_menu()
        option = int(input("Choose option to take action(1, 2, 3, 0): "))

        if option == 0:
            print("The program ended. Goodbye!")
            break
        elif option == 1:
            add_guest()
        elif option == 2:
            delete_guest()
        elif option == 3:
            guests_list()
        else:
            # This runs if the user enters a number like 9 or 5
            print("\n[!] Invalid option. Try again with 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()
