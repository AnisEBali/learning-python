tooLongText = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, 
but also the leap into electronic typesetting - remaining essentially unchanged. 
It was popularised in the 1960s with the release of_Letraset sheets_containing Lorem Ipsum passages, 
and more recently with desktop publishing software like_Aldus PageMaker_including versions of Lorem Ipsum.
'''
# Make text entirely lowercase:
def lowercase(text):
    return text.lower()

# Remove all punctuation marks
def removePunctuation(text):
    punctuations = ['.',',','-','_']
    for punctuation in punctuations:
        text = text.replace(punctuation,' ')
    return text

def removeNewLines(text):
    text = text.replace('\n',' ')
    return text

def removeLongWords(text):
    return' '.join([word for word in text.split() if len(word) < 6])
    #.split() = splits the text/string into a list of words
    #word for word in text... = take the words of the word list of text 
    #if len(word) < 6 = if they are less than 6 characters
    #' '.join = glue the words in the list back with ' ' spaces (sentences!)

#You can create a list with functions, the order doesn't matter! 
#Every function will be called which is practical
processingFunction = [removePunctuation, lowercase, removeLongWords]

for funct in processingFunction:
    tooLongText = funct(tooLongText)

print(tooLongText)

#Function with no name = Lambda function
print((lambda x: x + 4)(6))

myList = [5, 6, 4, 3]
print(sorted(myList))
#-> Result: [3, 4, 5, 6]

#You can use lambda to take the value of what is not normally sortable, and make it sorted:
anotherList = [{'num' : '3'}, {'num' : '2'}, {'num' : '1'}]
#Just doing print(sorted(myList)) here would cause an error (dictionaries can't be), instead:
print(sorted(anotherList, key=lambda x: x['num']))
#Key is to tell how it sorts, since key is 'num' in the dictionary, so look at the keys
#For every x in the list, return x['num'] which sort by the value attached by the key
#We don't use values for this sorting because the values are all different (and value = doesn't exist anyway)
#-> Result = [{'num': '1'}, {'num': '2'}, {'num': '3'}]
