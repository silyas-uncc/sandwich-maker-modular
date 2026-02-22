import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  Main program loop for the sandwich maker ###
    is_on = True

    while is_on:
        choice = input("What would you like? (small/medium/large): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {resources['bread']} slices")
            print(f"Ham: {resources['ham']} slices")
            print(f"Cheese: {resources['cheese']} ounces")
        elif choice in recipes:
            sandwich = recipes[choice]
            # Check resources
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                # Process payment
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    # Make sandwich
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice. Please choose small, medium, or large, report, or off.")

if __name__=="__main__":
    main()
