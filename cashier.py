class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        try:
            large_dollars = int(input("how many large dollars?: "))
            half_dollars = int(input("how many half dollars?: "))
            quarters = int(input("how many quarters?: "))
            nickels = int(input("how many nickels?: "))
            
            total = (large_dollars * 1.0) + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)
            return total
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return 0

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
