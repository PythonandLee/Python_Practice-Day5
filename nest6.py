# Create dictionaries in dinctionary to make abundant informatiom.
cities = {

    'rio': {
        'country': 'brazil',
        'population': 6688930,
        'time': 'UTC-3',
        },
        
    'copenhagen': {
        'country': 'denmark',
        'population': 777218,
        'time': 'UTC+01',
        },
        
    'dublin': {
        'country': 'ireland',
        'population': 554554,
        'time': 'UTC0',
        },
        
     }

# Define specific keys to change them into 'str()', 'title()', etc.     
for city, infos in cities.items():
    print("\nAbout " + city.title() + ":")

    country = infos['country']
    population = infos['population']
    time = infos['time']
    print("\tCountry: " + country.title())
    print("\tPopulation: " + str(population))
    print("\tTime: " + time)
        