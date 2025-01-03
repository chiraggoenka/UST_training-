items = [
    ['Bread', 40],
    ['Cookies', 80],
    ['Butter', 120],
    ['Cheese', 180],
    ['Yoghurt', 60]
]
cart = []  # Use a list to store cart items

while True:
    print("\nWhat do you want to do?")
    print("1. View items")
    print("2. Add items to cart")
    print("3. Update items in cart")
    print("4. Delete items from cart")
    print("5. Print bill")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nItems available:")
        for item in items:
            print("Name: " + item[0] + " Price: " + str(item[1]))

    elif choice == 2:
        item_name = input("Enter the item name: ")
        for item in items:
            if item[0] == item_name:
                quantity = int(input("Enter the quantity: "))
                for cart_item in cart:
                    if cart_item[0] == item_name:
                        cart_item[1] += quantity
                        break
                else:
                    cart.append([item_name, quantity, item[1]])
                print(f"{item_name} added to cart.")
                break
        else:
            print("Item isgir  not found.")

    elif choice == 3:
        item_name = input("Which item to be updated: ")
        for cart_item in cart:
            if cart_item[0] == item_name:
                quantity = int(input("Enter the quantity to be updated: "))
                cart_item[1] = quantity
                print(f"{item_name} updated in the cart.")
                break
        else:
            print("Item not in cart.")

    elif choice == 4:
        item_name = input("Which item to be removed: ")
        for cart_item in cart:
            if cart_item[0] == item_name:
                cart.remove(cart_item)
                print(f"{item_name} removed from cart.")
                break
        else:
            print("Item not in cart.")

    elif choice == 5:
        print("\nBill details:")
        total_amount = 0
        for cart_item in cart:
            name, quantity, price = cart_item
            total = price * quantity
            print(f"{name}, {quantity}, {price}, {total}")
            total_amount += total
        print(f"Total Amount of Bill: {total_amount}")

    elif choice == 6:
        print('thank you for shopping')
        break

    else:
        print("Invalid choice. try again.")

