#Assignnemt
x = "hello"
print(x)

#User Input
name = input("who are you? ")
print("Welcome", name)

#Elevator Floor Conversion Program
inp = input("Europe Floor?") 
usf = int(inp) + 1
print("US Floor", usf)

#Finding pay amount program
hrs = input("Enter hours you have worked: ")
rate = input("Enter rate Per hour: ")
pay = float(hrs) * float(rate) #converting to float/interger to multiply as input returns string by default
print("Pay:", pay) #Comma is a must for multiple printing

#Conditional Execution & Indention
#Program 1
x = 5
if x < 10:
    print("Smaller")
if x > 20:
    print("bigger")
print("Finish")

#Program 2
x = 42
if x > 1:
    print("More than one")
    if x < 100:
        print("Less than 100")
print("all done")

#Program 3 - If else
x = 4
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("Done")

