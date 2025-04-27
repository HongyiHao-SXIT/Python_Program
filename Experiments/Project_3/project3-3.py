product_list = {
    "Apple": 5,
    "Banana": 3,
    "Milk": 8,
    "Bread": 6,
    "Chocolate": 10
}

while True:
    try:
        budget = float(input("Please enter your shopping budget (in yuan): "))
        if budget < 0:
            print("The shopping budget cannot be negative. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("The product list is as follows:")
for index, (product, price) in enumerate(product_list.items(), start=1):
    print(f"{index}. {product}: {price} yuan")

purchased_products = []

while True:
    choice = input("Please enter the product number you want to buy (enter 'q' to quit): ")
    if choice.lower() == 'q':
        break
    try:
        choice = int(choice)
        if 1 <= choice <= len(product_list):
            product = list(product_list.keys())[choice - 1]
            price = product_list[product]
            if budget >= price:
                purchased_products.append(product)
                budget -= price
                print(f"Successfully purchased {product}. Remaining budget: {budget} yuan")
            else:
                print("Insufficient funds. You cannot purchase this product.")
        else:
            print("Invalid product number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid product number or 'q' to quit.")

if purchased_products:
    print("The products you purchased are as follows:")
    for product in purchased_products:
        print(product)
    print(f"Remaining budget after purchase: {budget} yuan")
else:
    print("You didn't purchase any products.")