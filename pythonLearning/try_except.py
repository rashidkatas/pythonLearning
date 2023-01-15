#Error Demonstration program
astr = 'Hello Rashid'
istr = int(astr) #Error, can't convert string to integer and program halts
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

#Error Handling program
astr = 'Hello Rashid'
try:
    istr = int(astr) #Dangerous code which will fail and will get ignored
except:
    istr = -1 #-1 is just a flag to show something was wrong above
print('First', istr)
astr = '123'
try:
    istr = int(astr) #This will be successfully
except:
    istr = -1 #This will be ignored
print('Second', istr)


#try block
astr = "Bob"
try:
    print("Hello")
    istr = int("astr") #this will fail, dangerous part
    print("There") #this will not run in the try block and will be ignored
except:
    istr = -1
print("Done", istr)

#real world example of getting input from user and handle with try/except
rawstr = input("Enter a number: ") #dangerous part as user may enter words instead of number
try:
    ival = int(rawstr) #converting input to int as result of input is always a string
except:
    ival = -1 #just a flag
if ival > 0:
    print("Nice Work")
else:
    print("Not a number")

