import random

# This function creates a 12 character long password containing letters, numbers, and characters
def passwordGenerator():
    letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    numbers = '1,2,3,4,5,6,7,8,9,10'
    characters = '!,@,#,$,%,&,*'
    password = ''
    placeCount = 0
    for i in range(8):
        if placeCount < 2:
            password += random.choice(letters.split(','))
            password += random.choice(numbers.split(','))
            password += random.choice(characters.split(','))
            placeCount += 1
            continue
        elif placeCount < 3:
            password += random.choice(numbers.split(','))
            password += random.choice(characters.split(','))
            password += random.choice(letters.split(','))
            placeCount += 1
            continue
        elif placeCount < 4:
            password += random.choice(characters.split(','))
            password += random.choice(letters.split(',')).upper()
            password += random.choice(numbers.split(','))
            placeCount += 1
            continue
    return password

# This asks the user for the number of passwords to generate and prints them
numPasswords = int(input('How many passwards to generate? '))
for i in range(1, numPasswords+1):
    pd = passwordGenerator()
    print(f'Password #{i}: {pd}')
