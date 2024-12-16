import os
import random

def pfandcode_creater_v1():
    print("\nPepsi 1.5L Code Generator")
    start_numbers = ["400", "410", "730", "900"]  # Country designations: 1.Germany, 2.Germany, 3.Sweden, 4.Austria
    middle_numbers = ["5678"]  # Company number
    end_number = ["90123"] # Article number

    repeat_count = int(input("How many codes should be created? "))
    for _ in range(repeat_count):
        random_start_number = random.choice(start_numbers)
        random_middle_number = random.choice(middle_numbers)
        random_end_number = random.choice(end_number)

        print(random_start_number , random_middle_number , random_end_number)
    input("Press Enter to return to the menu...")

def tool_two():
    print("\nWelcome to Tool 2!")
    print("This is where your tool logic could be.")
    input("Press Enter to return to the menu...")


def main_menu():
    while True:
        print("\n--- Menu Pfandcode Generator ---")
        print("1. Pepsi 1.5L Code Generator")
        print("2. Start Tool 2")
        print("3. Finish")

        choice = input("Wähle eine Option (1-3): ")

        if choice == "1":
            pfandcode_creater_v1()
        elif choice == "2":
            tool_two()
        elif choice == "3":
            print("Program is terminated. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main_menu()
