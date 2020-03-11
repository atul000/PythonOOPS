# A Dictionary is a collection which is unordered, changeble and indexed. No duplicate members.

person = {
    'first_name': 'Atul',
    'last_name': 'Beniwal',
    'age': 20
}

# Access value
print(person['first_name'])
print(person.get('last_name'))

# Add key/Value
person['phone'] = '12345'

# Get Keys
print(person.keys())

# Get Values
print(person.items())

# Make Copy
person2 = person.copy()
person2['city'] = 'Delhi'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
# person.clear()

# Get Length
print(len(person2))

print(person)

# List of dict
people = [
    {'name': 'Alex', "age": 33},
    {'name': 'Jos', "age": 32}
]
print(people[1]['name'])
