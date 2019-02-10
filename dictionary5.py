# Use '{}' as dictionary, and insert valuation to print.
favorite_language = {
    'roy': 'python',
    'jim': 'java',
    'frank': 'c',
    'tina': 'ruby',
    }
# Use 'for-in' to pass all keys and values. 
# Remember to add '.items()' to reall keys and values in the dictionary.   
for name, language in favorite_language.items():    
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")
print('\n')        
# Use 'keys()' to pass only keys in dictionary.
for name in favorite_language.keys():
    print(name.title())
