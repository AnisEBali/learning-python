print(bytes(4))
#This creates a byte object that is 4 bytes long
#Response = b'\x00\x00\x00\x00'
#-> It's in hexidecimal, but in ASCII form !!!!!! Not raw hexidecimal
#-> All 4 bites are empty.
#-> b' is to differentiate byte objects from strings

#You can insert numbers into it:
numberBytes = bytes([14,2,97,7])
print(numberBytes)
#Result = b'\x0e\x02a\x07'
#-> ASCII: x0e = 14, x02 = 2, a = 97, x07 = 7
#ASCII because it's easier to read, especially the bigger numbers.

#Since it's ASCII:
fireEmoji = bytes('🔥','utf-8')
#Emoji is a string so it needs to be between ' '!
#You still need to declare in this case, which format it is
#Otherwise it will throw a Syntax Error
#Emojis are coded in Unicode transformation format (utf-8)
print(fireEmoji)
#Result = b'\xf0\x9f\x94\xa5' = byte emoji

print(fireEmoji.decode('utf-8'))
#This will print the emoji directly onto the VS Code's terminal 
#It does not show on Command Prompt though

#We can even change the emoji:
#Change it first into an array otherwise it won't act like a list:
fireEmoji = bytearray('🔥','utf-8')
#Now it acts like a list:
fireEmoji[3] = int('a1',16)
print(fireEmoji.decode('utf-8'))
#Changes it onto ABCD emoji in the terminal