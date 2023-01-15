#While Loop
n = 5
while n > 0:
    print(n)
    n = n - 1 #Loop controler
print('Is not greater anymore')
print(n)


#Using break to end loop
while True: #not True starts with capital T
    line = input('> ')
    if line == 'done':
        break #will break only if input is written as "done", otherwise will print whatever inputed
    print(line)
print('Done!!')

#using continue to skip iteration and go to the next iteration
while True:
    line = input('> ')
    if line[0] == '#': #checking if first character inputed is #
        continue #skip(ignore next line) and go back on top of loop and continue with next iteraton
    if line == 'done':
        break #get out of loop for good
    print(line) # this will be printed for every input except above conditions
print('Done!!') #output when loop is broken

#example1
#for loop or definite loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff')

#example2
friends = ['Issa', 'Mussa', 'Juma'] #set of friends
for friend in friends:
    print('Happy New Year:',friend)
print('2023!!')
