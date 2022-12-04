#POWER CALCULATOR
#HEADINGS
print("POWER CALCULATOR")

#THE PROGRAM
try:
    basenum = float(int(input("input your base number below \n")))
except ValueError:
    print('Error')
power = (float(int(input("your power below \n"))))
answer = pow(basenum, power)
print(answer)
print("This is your answer thanks")

