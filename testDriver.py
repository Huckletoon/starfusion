import json
import string

test = json.load(open('races.json','r'))

#print(test)
#builder = []
#builder.append('Here\'s a list of all the playable **Races** for our campaign:\n\n')
builder = 'Here\'s a list of all the playable **Races** for our campaign:\n\n'
msgs = []

for race in test:
    builder += '**' + string.capwords(race, '-') + '**: ' + test[race]['shortDesc'] + '\n\n'
    if len(builder) >= 200:
        temp = builder
        msgs.append(temp)
        builder = ''
    
#msgs.append(builder)


counter = 0
for msg in msgs:
    print(str(counter) + '-----')
    print(msg)
    counter+= 1
