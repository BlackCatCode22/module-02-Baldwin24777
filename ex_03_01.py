
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if  fh > 40:
    # print("Overtime")
    reg = fh * fr
    otp = (fh - 40) * (0.5 * fr)
    # print(reg, otp)
    xp = reg + otp
    print(xp)
else:
    # print("Regular")
    xp = fh * fr
print("Pay:",xp)

# Anthony Baldwin 








