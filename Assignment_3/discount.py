def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        print("The final price after applying the discount is: Kshs", final_price)
        return final_price
    
    else:
        print ('This product is not on sale. The final price is still Kshs', price)
        return price
    
    
original_price = float(input("Enter the price of the item: Kshs "))
discount_percentage = float(input("Enter the discount (%): "))

final_price = calculate_discount(original_price, discount_percentage)
