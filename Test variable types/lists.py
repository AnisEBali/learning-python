my_list = [1,2,3,4]
print(my_list)

your_list = ['list','of','things']
print(your_list)

len(my_list)
# Won't work on its own

print(len(my_list))

#Let's experiment lists and complex numbers
complex_list = [1 + 5j, 2 + 6j]
#print(complex_list.real)
#print(complex_list.imag)
#Doesn't work! One list item at a time
print(complex_list[0].real)
print(complex_list[1].real)
print(complex_list[0].imag)
print(complex_list[1].imag)

#Inner lists
inner_list = [[1,2,3],[True,False]]
print(inner_list)
#This has 3 elements
three_list = [[1,2], [True,True], []]
print(len(three_list))
