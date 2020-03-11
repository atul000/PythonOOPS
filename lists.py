# a list is a collection which is ordered and changeble. allows duplicate members.

numbers = [1, 2, 3, 4]

fruits = ['apples', 'oranges', 'grapes', 'guava', 'pineapple']

# get value
print(fruits[1])

# get len
print(len(fruits))

# append something
fruits.append('mangos')

# insert into position
fruits.insert(2, 'banana')

# remove from position
fruits.pop(1)

# reverse list
fruits.reverse()

# sort items
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

# remove from list
fruits.remove('grapes')
print(fruits)
