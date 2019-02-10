# Use dictionary to store a series of information.
# If want to make a new line, press enter after '+'.
# When to print numbers, remember to add 'str()'.

drink = {'first_name': 'black tea',
    'last_name': 'bag',
    'age': 2500,
    'place': 'india',
    }
    
print("One of my favorite tea is " +
    drink['first_name'] + " " + drink['last_name'] + 
    " ,and the history \nwe drink it has been last for " +
    str(drink['age']) + " years \nand the place of production is " +
    drink['place'].title() + ".")