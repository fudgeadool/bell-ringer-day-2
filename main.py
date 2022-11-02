coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

#retrieve the names and price from the above tuple

for coffee, price in coffee_prices:
  print(f"coffee {coffee} and price ${price}")

  # if .9 - .5 - .2:
  #  print("mocha,1.9")


def most_expensive_coffee(coffee_prices):
  highest_price = 0
  my_most_expensive_coffee = ''
  for coffee, price in coffee_prices:
   if price > highest_price:
     highest_price = price
     my_most_expensive_coffee = coffee
   else:
     pass
  return(my_most_expensive_coffee,highest_price)
print(most_expensive_coffee(coffee_prices))
