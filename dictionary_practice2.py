# Use '{}' as dictionary, and insert valuation to print.
# Use list to recall dictionary can distinguish users.
favorite_language = {
    'roy': 'python',
    'jim': 'java',
    'frank': 'c',
    'tina': 'ruby',
    }
survey = ['oscar', 'tina', 'elisia', 'winston']

for name in favorite_language:
    if name in survey:
        print("Thank you, " + name.title() + ", for joining our survey.")
    else:
        print(name.title() + ", please do join us next time.")
