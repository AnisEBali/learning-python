a = True
if a : 
    print('It is true!')

b = False
if b :
    print('It is true too!')
#b doesn't show up

c = True
if c :
    print('This is also true!')
    print('This is an indent')

#complex identation

e = True
f = False
g = True
if e :
    print('This one is true!')
    if f: 
        print('They are both true')
        if g:
            print('All three are true!')
else:
    print('It is false!')
print('This is a control!')
#Only up to the print of e variable + control does it show 
#else is under e that's why it doesn't show 

m = True
n = False
if m:
    print('m is telling the truth!')
    if n: 
        print('n is telling the truth!')
    else: 
        print('n is lying...')
else: 
    print('m is lying...')
#if m was lying, it wouldn't have checked if n was lying or not
