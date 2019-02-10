# Create lists in dictionary to add more values.
favorite_nums = {
    'patric': [987, 52, 45544],
    'louise': [21, 577, 5],
    'andy': [1, 6, 22]
    }

# Use for to pass all keys and values.    
for friend, numbers in favorite_nums.items():
    print("\nThree favorite numbers of " + friend.title() + " are:")
    for number in numbers:
        print("\t" + str(number))