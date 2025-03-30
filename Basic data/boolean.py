print(bool(1))
#Returns True

print(bool(0))
#Returns False

print(bool(-1))
#Returns True too

print(bool('False'))
#Returns True, all strings do except:
print(bool(''))
#^This is False, but:
print(bool(' '))
#^This is True

bool([1,2])
#Returns True
bool([])
#Returns False
bool(None)
#Returns False

#If-statements are boolean statements by default
myList = [1,2]
if myList:
    print('Mylist has values in it!')

yourList = []
if yourList:
    print('Yourlist has values in it!')

a = 5
b = 5
if a - b:
    print('a and b are not equal')
if a == b:
     print('a and b are equal')

weatherIsNice = False
haveUmbrella = True
if not haveUmbrella or weatherIsNice:
    print('Stay inside')
else:
    print('Go for a walk')
#Response = 'Go for a walk'
#Logic is correct, but the if not function checks for the first parameter which can create issues:

weatherIsNice = True
haveUmbrella = False
if not haveUmbrella or weatherIsNice:
    print('Stay inside')
else:
    print('Go for a walk')
#Response = 'Stay inside'
#weatherIsNice got ignored because only haveUmbrella got impacted by not

#To fix this:
weatherIsNice = True
haveUmbrella = False
if not (haveUmbrella or weatherIsNice):
    print('Stay inside')
else:
    print('Go for a walk')