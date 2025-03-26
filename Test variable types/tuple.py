#lists can be appended
new_list = [1,2,3]
new_list.append(4)
print(new_list)

#tuples cannot be appended!
my_tuple = (1,2,3)
#my_tuple.append(4) = AttributeError
print(my_tuple)

#previous print won't show 5, the next print does
new_list.append(5)
print(new_list)

#print(new_list.append(6)) = doesn't work

