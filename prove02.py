print ('Please enter the following:')
print(' ')#insert space
adjective = input('adjective: ')
animal = input('animal: ')
verb = input('verb: ')
exclamation = input('exclamation: ')
verb1 = input('verb: ')
verb2 = input('verb: ')
print(' ')#insert space
print('Your story is: ')
print(' ') #insert space
#Print paragragh with inserted strings.
output = f' The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb1.lower()} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2.lower()} right in front of my family.' 
print(output)