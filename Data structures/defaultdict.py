from collections import defaultdict

desserts = {
    'a' : ['apple pie'],
    'b' : ['baked alaska','banana pudding'],
    'c' : ['cheesecake'],
}

#First you have to give the type what you want to return:
desserts = defaultdict(list)

print(desserts)
# -> Result: defaultdict(<class 'list'>, {})
#Defaultdict is still empty

desserts['d'].append('donut')
print(desserts)
# -> Result: defaultdict(<class 'list'>, {'d': ['donut']})
#We didn't have to define the entry as a list entry (see fruits['d'] = ['date'])
#Defaultdict already did that

desserts['d'].append('dulce de leche')
print(desserts)
# -> Result: defaultdict(<class 'list'>, {'d': ['donut', 'dulce de leche']})

print(desserts['f'])
# -> Result: [], empty list, no error!