from datetime import datetime

print(datetime.now().second)
#= how many seconds into the current minute

print(datetime.now().second + 2)
#= 2 seconds past the current second into the minute

#Careful with 59 seconds otherwise it turns into 61 seconds:
print((datetime.now().second + 2) % 60)
#So it resets to 0 if it's 58 seconds

#While loop to print out some message while waiting 2 seconds:

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    #print('Still waiting...')
    #This is bad idea because Python can print a lot in 2 seconds!!!
    #We still need something so do this:
    pass
print(f'We are at {wait_until} seconds!')

wait_threeSeconds = (datetime.now().second + 3) % 60

while True:
    if datetime.now().second == wait_threeSeconds:
        print(f'We are at {wait_threeSeconds} seconds!')
        break
#While True loops infinitely
#When if statement is fullfiled, break immediately ends the loop so it doesn't goes on!

wait_fourSeconds = (datetime.now().second + 4) % 60

while datetime.now().second != wait_fourSeconds:
    continue
    print('Still waiting')
    #^This gets ignored because continue which makes the function whatever comes next in identation
print(f'We are at {wait_fourSeconds} seconds!')

#Continue + break

wait_fiveSeconds = (datetime.now().second + 5) % 60

while True:
    if datetime.now().second < wait_fiveSeconds:
        continue
    break
print(f'We are at {wait_fiveSeconds} seconds!')
#-> As long as the waiting time is not hit, continue is hit which makes the break ignored and while loop keep looping
#-> When the if statement is no longer, continue is ignored and break makes the while loop stop 
