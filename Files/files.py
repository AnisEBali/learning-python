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
