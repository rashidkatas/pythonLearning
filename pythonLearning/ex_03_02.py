#writing pay program using try and except to handle non-numeric input gracefully by giving message
h = input("Enter Hours: ")
r = input("Enter Rate: ")
try:
    fh = float(h)
    fr = float(r)
except:
    fh = -1
    fr = -1
    print("Error, please enter numeric input") #indention here is very crucial
    exit() #exit program and stop #indention here is very crucial to end based on except or use quit()
if fh > 40:
    print("Overtime")
    reg = fh * fr
    ovrt = (fh - 40.0) * (fr * 0.5) #overtime
    print(reg, ovrt)
    pay = reg + ovrt
else:
    print("Regular")
    pay = fh * fr
print("Pay:", pay)
