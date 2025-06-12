from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant
from Models.Cart import Cart

class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants()

    def __PrepareFoodItems(self):
        return [
            FoodItem("Veg Biriyani", 4.5, 100, "Good"),
            FoodItem("Chicken Biriyani", 4.6, 150, "Very Good"),
            FoodItem("Mutton Biriyani", 4.9, 200, "Excellent"),
            FoodItem("Parota", 4.0, 20, "Nice"),
            FoodItem("Noodles", 4.5, 80, "Good"),
            FoodItem("Chicken Noodles", 4.5, 120, "Good"),
            FoodItem("Chicken Gravy", 4.5, 180, "Good")
        ]

    def __PrepareFoodMenus(self):
        items = self.__PrepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [items[0], items[4]]
        menu2 = FoodMenu("Non-Veg")
        menu2.FoodItems = [items[1], items[2], items[5], items[6]]
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [items[3]]
        return [menu1, menu2, menu3]

    def __PrepareRestaurants(self):
        menus = self.__PrepareFoodMenus()
        res1 = Restaurant("A2D", 4.5, "Trichy", 10)
        res1.FoodMenus = [menus[0]]
        res2 = Restaurant("Muniyandi Vilas", 4.6, "Salem", 20)
        res2.FoodMenus = [menus[0], menus[1]]
        res3 = Restaurant("KFC", 4.4, "Dharmapuri", 25)
        res3.FoodMenus = [menus[1], menus[2]]
        res4 = Restaurant("Meat & Eat", 4.7, "Namakkal", 30)
        res4.FoodMenus = [menus[1]]
        return [res1, res2, res3, res4]

    def FindRestaurant(self, name):
        for res in self.Restaurants:
            if res.Name.lower() == name.lower():
                return res