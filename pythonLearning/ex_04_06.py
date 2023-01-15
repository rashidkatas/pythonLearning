#defining a function to calculate pay
def computepay(hours, rate):   
    if hours > 40:
        print("Overtime")
        reg = hours * rate
        ovrt = (hours - 40.0) * (rate * 0.5) #overtime
        pay = reg + ovrt 
    else:
        print("Regular")
        pay = hours * rate
    return pay
#end of function definition

#receiving int inputs and producing float
h = input("Enter Hours: ")
r = input("Enter Rate: ")
fh = float(h)
fr = float(r)
xp = computepay(fh, fr) #calling function
print("Pay:", xp) #printing final output either overtime or regular