"""
Name: Rekha Shekhawat
Description: Command line Shopping List application with file persistence.
"""

import os


class ShoppingList:
    def __init__(self):
        """Initialize state and load items from file."""
        self.filename = "shopping_list.txt"
        self.items = []
        self.load_items()

    def start_menu(self):
        """Print menu instructions."""
        print("What do you want to add to your shopping list?")
        print("Enter 'DONE' to stop adding items.")
        print("Enter 'HELP' for additional info.")
        print("Enter 'SHOW' to see your shopping list.")
        print("Enter 'REMOVE' to remove an item from your shopping list.")
        print("-----------------------------------------")

    def normalize_item(self, item):
        """Capitalize first letter and lowercase the rest."""
        return item.strip().capitalize()

    def add_to_list(self, item):
        """Add item if not already present."""
        item = self.normalize_item(item)

        if item in self.items:
            print(f"{item} already exists in your shopping list.")
        else:
            self.items.append(item)
            print(f"{item} was added to your shopping list.")
            print(f"You have {len(self.items)} items on your list.")

    def remove_item(self, item):
        """Remove item if present."""
        item = self.normalize_item(item)

        if item in self.items:
            self.items.remove(item)
            print(f"{item} was removed from your shopping list.")
            print(f"You have {len(self.items)} items on your list.")
        else:
            print(f"{item} was not found in your shopping list.")

    def show_shopping_list(self):
        """Display shopping list."""
        print("My Shopping List:")
        if not self.items:
            print("(Your shopping list is empty.)")
        else:
            for item in self.items:
                print(f"- {item}")

    def save_items(self):
        """Write items to file."""
        try:
            with open(self.filename, "w") as file:
                for item in self.items:
                    file.write(item + "\n")
            print("Your shopping list has been saved.")
        except IOError:
            print("Error saving shopping list.")

    def load_items(self):
        """Read items from file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    self.items = [line.strip() for line in file if line.strip()]
        except IOError:
            print("Error loading shopping list file.")

    def command_loop(self):
        """Main input loop."""
        self.start_menu()

        while True:
            try:
                user_input = input("> ").strip()

                if not user_input:
                    continue

                command = user_input.upper()

                if command == "DONE":
                    print("See you soon!")
                    self.save_items()
                    self.show_shopping_list()
                    break

                elif command == "HELP":
                    self.start_menu()

                elif command == "SHOW":
                    self.show_shopping_list()

                elif command == "REMOVE":
                    self.show_shopping_list()
                    item_to_remove = input("What do you want to remove?: ")
                    self.remove_item(item_to_remove)

                else:
                    self.add_to_list(user_input)

            except EOFError:
                print("\nEOF received. Saving and exiting...")
                self.save_items()
                break


def main():
    shopping_list = ShoppingList()
    shopping_list.command_loop()


if __name__ == "__main__":
    main()