#This uses Recursion: 
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)
#Recursion means the function calls itself until base case (num == 1) is met

def square(num):
    return triangle(num) + triangle(num-1)

print(square(6))
