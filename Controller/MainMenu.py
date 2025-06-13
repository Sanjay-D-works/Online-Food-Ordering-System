from Controller.FoodManager import FoodManager
from Models.Cart import Cart

class MainMenu:

    __Options = {
        1: "show_restaurants",
        2: "show_food_items",
        3: "search_restaurant",
        4: "search_food_item",
        5: "logout"
    }

    def __init__(self):
        self.__food_manager = FoodManager()

    def show_restaurants(self):
        for i, res in enumerate(self.__food_manager.Restaurants, 1):
            res.DisplayItem(i)

        try:
            choice = int(input("Please select the restaurant: ")) - 1
            if 0 <= choice < len(self.__food_manager.Restaurants):
                res = self.__food_manager.Restaurants[choice]
                self.show_food_menus(res.FoodMenus)
            else:
                print("Invalid restaurant selection.")
        except ValueError:
            print("Invalid input.")

    def show_food_items(self, food_items=None):
        if food_items is not None:
            for i, item in enumerate(food_items, 1):
                item.DisplayItem(i)

            try:
                choices = list(map(int, input("Choose your food items (e.g., 1,2): ").split(',')))
                cart = Cart(food_items, choices)
                cart.ProcessOrder(food_items)
            except (ValueError, KeyError):
                print("Invalid selection.")
        else:
            print("No food items to display.")

    def search_restaurant(self):
        name = input("Enter restaurant name: ")
        res = self.__food_manager.find_restaurant(name)

        if res:
            print("Restaurant found:")
            res.DisplayItem()
            self.show_food_menus(res.FoodMenus)
        else:
            print(f"No restaurant found with name '{name}'")

    def search_food_item(self):
        print("Feature not implemented yet.")

    def show_food_menus(self, menus):
        print("\nAvailable Menus:")
        for i, menu in enumerate(menus, 1):
            menu.DisplayItem(i)

        try:
            choice = int(input("Choose menu: ")) - 1
            if 0 <= choice < len(menus):
                self.show_food_items(menus[choice].FoodItems)
            else:
                print("Invalid menu selection.")
        except ValueError:
            print("Invalid input.")

    def logout(self):
        print("Logging out...")
        exit(0)

    def start(self):
        while True:
            print("\nMain Menu")
            for key, value in MainMenu.__Options.items():
                print(f"{key}. {value.replace('_', ' ').title()}")

            try:
                choice = int(input("Enter your choice: "))
                action = getattr(self, MainMenu.__Options.get(choice, ""), None)
                if action:
                    action()
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
