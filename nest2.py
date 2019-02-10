favorite_language = {
    'roy': ['python', 'c'],
    'jim': ['java'],
    'frank': ['c', 'javascript'],
    'tina': ['ruby', 'html', 'php'],
    }
 
x, y = 'are', 'is'
for name, languages in favorite_language.items():    
    if len(languages) > 1: 
        print("\n" + name.title() + "'s favorite languages " + x + ":") 
    else:
        print("\n" + name.title() + "'s favorite language " + y + ":")
    for language in languages:
        print(language.title())
 