db = {
        'name':'Zed',
        'age':39,
        'height':6*12 + 2
     }

print(db['name'])
print(db['age'])
print(db['height'])
db['city'] = 'SF'
print(db['city'])

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print(f"NY State has: {cities['NY']}")
print(f"OR State has: {cities['OR']}")

print('-' * 10)
for key, value in cities.items():
    print(f"{key} has the city {value}")

print('-' * 10)
for state, abb in states.items():
    print(f"{state} state is abbreviated {abb}")
    print(f"and has city {cities[abb]}")

state = states.get('Texas')
if not state:
    print('Sorry, no Texas.')

city = cities.get('TX', "Does not exist")
print(f"The city for the state 'TX' is: {city}")