class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize CashRegister with an optional discount percentage.

        Args:
            discount (float, optional): The discount percentage to apply. Defaults to 0.
        """
        self.discount = discount
        self.total = 0
        self.last_transaction_amount = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        """
        Add an item with a given title, price, and optional quantity to the total.

        Args:
            title (str): The title of the item.
            price (float): The price of the item.
            quantity (int, optional): The quantity of the item. Defaults to 1.
        """
        total_price = price * quantity
        self.total += total_price
        self.last_transaction_amount = total_price
        self.items.append((title, price, quantity))

    def apply_discount(self):
        """
        Apply discount to the total based on the discount_percentage.
      
        Returns:
            float: The discounted total after applying the discount.
        """
        if self.discount == 0:
            print("There is no discount to apply.")
            return self.total
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total:.0f}.")
        return self.total

    def void_last_transaction(self):
      """Remove the last transaction amount from the total."""
      if self.items:
        last_item_price = self.items[-1][1] * self.items[-1][2]  # Calculate the total price of the last item
        self.total -= last_item_price
        self.last_transaction_amount = last_item_price
        self.items.pop()  # Remove the last item from the items list
