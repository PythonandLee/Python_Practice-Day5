aliens = []
# Use 'append()' to add elements in the list.
for new_alien in range(30):
    new_alien = {'color' : 'green', 'point' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Use the method below to change values.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10

# Finally, deciede the amount we want to print.    
for alien in aliens[:5]:
    print(alien)   
print('...')
# Reveal how many all aliens are.    
print("Total number of aliens: " + str(len(aliens))) 