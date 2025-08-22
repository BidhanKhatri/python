cart = {
    "apple": (2.5, 4),  # price per item, quantity
    "milk": (1.5, 2),
    "bread": (2, 1)
}


def calculate_bill(cart):
    
    price_list = []
    quan_list = []

    for item in cart:     
        # print(cart.get(item)[0])
        price_list.append(cart.get(item)[0])
        quan_list.append(cart.get(item)[1])

        cart_item_price = cart.get(item)[0]
        cart_item_quantity = cart.get(item)[1]
        
        print(f"{item.capitalize()} x {cart_item_quantity}\nprice: {cart_item_price}")
        print("")

    total_price = sum(price_list)
    total_quantity = sum(quan_list)

    print(f"You total quantity is {total_quantity}")
    print(f"You total price is Rs {int(total_price)}")
    
   
        

calculate_bill(cart)    


