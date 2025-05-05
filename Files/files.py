f = open('some_text.txt', 'r')
print(f)
# File needs to be in the same folder
# -> Result: <_io.TextIOWrapper name='some_text.txt' mode='r' encoding='cp1252'>
# 'r' is for read-only

print(f.readline())
# -> Result: This is some text
# -> Reads one line and moves the cursor at the line of the line
# print(f.readline())
# -> This will read the second line, not the first
# -> Moves the cursor towards the third line.

print(f.readlines())
# -> Will read everything after the cursor in a list.
# -> Result: ["And there's another line here\n", "And here's another one too."]

#If we want to read everything without a list:
g = open('some_text.txt', 'r')
for line in g.readlines():
    print(line.strip())
# strip() is to remove ugly space after each line

# WRITING:
h = open('write_text.txt', 'w')
print(h)
# Creates the file automatically

h.write('Line 1\n')
h.write('Line 2\n')

h.close()
# Writing to a text puts the text first in a buffer and doesn't write to the file
# You have to close the file first! Then run the py file

# WRITING WITHOUT OVERWRITING = APPENDING
i = open('write_text.txt','a')

i.write('Line 3\n')
i.write('Line 4\n')

i.close()

# Closing files but can lead to unexpected behaviors
# Safest way to close a file without the possibility to write anything after:
with open('some_text.txt','a') as j:
    j.write('\nSome stuff.\n')
    j.write('Some other stuff.\n')

# We still have access to j's information
print(j)
# -> Result: <_io.TextIOWrapper name='some_text.txt' mode='a' encoding='cp1252'>
# BUT:
# j.write('PS. I forgot some stuff')
# This will no longer work and throw an error!
