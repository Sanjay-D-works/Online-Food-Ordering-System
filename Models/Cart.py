class Cart:

    def __init__(self, items, choices):
        self.Choices = choices
        self.FoodItems = self.__AddtoCart(items)

    def __AddtoCart(self, items):
        foodDic = {}
        for choice in self.Choices:
            if choice > len(items):
                raise KeyError
            foodDic[choice] = foodDic.get(choice, 0) + 1
        return foodDic

    def ProcessOrder(self, fooditems):
        Total = 0
        print("\n--- Order Summary ---")
        for item in self.FoodItems:
            price = self.FoodItems[item] * fooditems[item - 1].Price
            Total += price
            print(f"{fooditems[item - 1].Name} x {self.FoodItems[item]} = ₹{price}")
        print(f"\nTotal: ₹{Total}")
        self.ProcessPayment(Total)

    def ProcessPayment(self, amount):
        print("\nChoose Payment Method:")
        print("1. UPI\n2. Card\n3. Cash on Delivery")
        choice = input("Enter your choice: ")
        print(f"Payment of ₹{amount} done using option {choice}. Thank you!")