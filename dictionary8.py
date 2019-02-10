rivers = {
    'nile' : 'egypt',
    'gonga' : 'india',
    'saigon' : 'vietnam',
    }
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + 
        country.title() + ".")    