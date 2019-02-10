# Create dictionaries in dictiomary to make more than one informations.
users = {
    'scooper': {
        'first': 'sheldon',
        'last': 'cooper',
        'location' : 'texas',
        },
        
    'lhofstadter': {
        'first': 'leonard',
        'last': 'hofstadter',
        'location': 'new jersey',
        },
      }

# Define new valuation to dictionary values 
# which can easily change types and combine values.      
for username, user_inf in users.items():
    print("\nUsername: " + username)
    
    full_name = user_inf['first'] + " " + user_inf['last']
    location = user_inf['location'] 
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())