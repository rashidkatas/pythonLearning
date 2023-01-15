#receiving int inputs and producing float and calculate pay
h = input("Enter Hours: ")
r = input("Enter Rate: ")
fh = float(h)
fr = float(r)
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