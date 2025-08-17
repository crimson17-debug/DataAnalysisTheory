prices = [100 , 200, 300]

discount = 10

final_price = []

for price in prices:
    new_price = price - (price *discount/100)
    final_price.append(new_price) 


print(final_price)