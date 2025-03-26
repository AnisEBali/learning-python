my_dictionary = {
    'apple' : 'a red fruit',
    'pear' : 'a gross fruit'
}

print(my_dictionary['apple'])

conflict_dictionary = {
    'cat' : 'a goofy animal',
    'dog' : 'a happy animal',
    'cat' : 'a lazy animal'
}

print(conflict_dictionary['cat'])
# Will only show the latest entry 'a lazy animal'

two_entries = {
    'monday' : 'a hateful day',
    'friday' : 'the best day'
}
print(two_entries['friday']+ ", " + two_entries['monday'])

profile = {
    'name' : 'Anis',
    'skills' : {
        'python' : 'beginner',
        'design thinking' : 'advanced'
    }
}

print(profile['skills']['python'])
#will only python's definition
#print(profile['skills']) will show all 4 words