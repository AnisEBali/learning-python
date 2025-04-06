animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}

print(animals)
#-> Result: {'a': 'aardvark', 'b': 'bear', 'c': 'cat'}

#Show one specific entry:
print(animals['b'])
#-> Result: bear

#To add something:
#animals.append('d': 'dog') does not work!
animals['d'] = 'dog'
print(animals)
#-> Result: {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#Similar, replace something:
animals['a'] = 'antelope'
print(animals)
#-> Result: {'a': 'antelope', 'b': 'bear', 'c': 'cat', 'd': 'dog'}

#KEYS & VALUES
print(animals.keys())
#-> Result: dict_keys(['a', 'b', 'c', 'd'])
print(animals.values())
#-> Result: dict_values(['antelope', 'bear', 'cat', 'dog'])

#Copy the keys to a list
print(list(animals.keys()))
#-> Result: ['a', 'b', 'c', 'd']

#print(animals['e']) will throw an error because e does not exist, BUT
print(animals.get('e'))
#-> Result: None (instead of an Error)

#A DICTIONARY OF LIST
fruits = {
    'a': ['apple', 'appricot'],
    'b': ['banana'],
    'c': ['cherry'],
}
#Now we can append!
fruits['c'].append('coconut')
print(fruits)
#-> Result: {'a': ['apple', 'appricot'], 'b': ['banana'], 'c': ['cherry', 'coconut']}

#Create a new entry list
fruits['d'] = ['date']
print(fruits)
#-> Result: {'a': ['apple', 'appricot'], 'b': ['banana'], 'c': ['cherry', 'coconut'], 'd': ['date']}

#CAUTION WITH OVERWRITING IN BIG LISTS
if 'f' not in fruits:
    fruits['f'] = ['fig']

if 'c' not in fruits: 
    fruits['c'] = ['citron']

print(fruits)
#-> Result: