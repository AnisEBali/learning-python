class WordSet:
#__init__ is important to initialize the class and have objects using the class blueprint having all the attributes under the class
    def __init__(self):
        self.words = set()
        # = Set starts off empty
        # We can add to it
    
    def addText(self, text):
        text = self.cleanText(text)
        # = Calls another function too if this function is called
        for word in text.split():
            # Split function = splits the string by space and turns into list
            self.words.add(word)
            #Add the words split from the text into the set() words as defined above!

    def cleanText(self,text):
        # self here is not directly used, but it is still important since it connect this function to the current object
        # Removing it will cause an error!
        # Chaining functions:
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','') 
        return text.lower()
        # Makes everything lowercase


newWordSet = WordSet()

newWordSet.addText('Hi, I\'m Anis! Here is a sentence I want to add!')
newWordSet.addText('Here is another sentence I want to add.')

print(newWordSet.words)
# -> Result = {'want', 'hi', 'here', 'to', 'a', 'another', 'add', 'i', 'anis', 'is', 'sentence', 'im'}

# What if we want to remove self from cleanText(self,text) anyway?
class AnotherWordSet:
    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = AnotherWordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)
    # addText is still an INSTANCE METHOD = still highly dependable on self
            
    def cleanText(text):
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','') 
        return text.lower()
    # cleanText is now a STATIC METHOD = no longer linked to objects/self
    # = static methods are unchanged, they are for unchanging variables

evenNewerWordSet = AnotherWordSet()

evenNewerWordSet.addText('Hi, I\'m Anis! Here is a sentence I want to add!')
evenNewerWordSet.addText('Here is another sentence I want to add.')

print(evenNewerWordSet.words)


class LastWordSet:
    # STATIC VARIABLES = belonging to the class, not self/object
    replacePuncs = ['!','.',',','\'']

    def __init__(self):
        self.words = set()

    # Now that cleanText has a Decorator and Python knows what method it is:
    # We can freely use self.cleanText(text) without sending self to static method cleanText
    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    # Decorator = description for function definition:
    @staticmethod
    def cleanText(text):
        for punc in LastWordSet.replacePuncs:
            text = text.replace(punc,'')
        return text.lower()

latestWordSet = LastWordSet()

latestWordSet.addText('Hi, I\'m Anis! Here is a sentence I want to add!')
latestWordSet.addText('Here is another sentence I want to add.')

print(latestWordSet.words)