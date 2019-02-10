pizza = {
    'crust': 'thick',
    'toppings': ['oliver', 'extra cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the toppings:" )
for topping in pizza['toppings']:
    print('\t' + topping)  