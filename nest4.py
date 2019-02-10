# Create lists in dictionary to give more than one answers.
favorite_places = {
    'patric': ['beach', 'shopping mall', 'restauran'],
    'louise': ['church', 'school', 'foodball yard'],
    'andy': ['bed', 'beach', 'dance club']
    }

# Remember to add 'items()' when want to recall both 'key & value'.    
for friend, places in favorite_places.items():
    print("\nThree favorite places of " + friend.title() + " are:")
    for place in places:
        print("\t" + place)