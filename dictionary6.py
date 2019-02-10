# Use '{}' as dictionary, and insert valuation to print.
favorite_language = {
    'roy': 'python',
    'jim': 'java',
    'frank': 'c',
    'tina': 'ruby',
    'anjay': 'python',
    }
# Use 'for-in' to pass all keys and values. 
# Remember to add '.items()' to reall keys and values in the dictionary.   
for name, language in favorite_language.items():    
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")
print('\n')   
     
# Use 'keys()' to pass only keys in dictionary, but it is fine if not use it.
for name in favorite_language.keys():
    print(name.title())
print("\n")

# Create a list and insert the same keys in dictionary for our special users.
friends = ['roy', 'frank']
for name, language in favorite_language.items():
    if name in friends:
        print("Hello " + name.title() + ", glad you like " + 
            language.title() + ".")
    else:
        print(name.title())
print("\n")
        
# Use 'sorted()' in 'for-in' to sort keys in dictionary.
for name in sorted(favorite_language):
    print(name.title() + ", thank you for joining us!")
print('\n')    
    
# If only want to recall values, use 'values()'.
# ***Use 'set' when pass the dictionary can prevent to print values again.***
print("These are the languages people commonly like.")
for language in set(favorite_language.values()):
    print(language.title())
