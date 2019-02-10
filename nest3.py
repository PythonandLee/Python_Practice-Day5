# Create dictionaries in list, and recall the values.
user_1 = {
    'name': 'amy',
    'age': 33,
    'location': 'california',
    }
user_2 = {
    'name': 'bernadette',
    'age': 34,
    'location': 'california',
    }
user_3 = {
    'name': 'penny',
    'age': 34,
    'location': 'nebraska',
    }
    
people = [user_1, user_2, user_3]

for user in people:
    print(user)