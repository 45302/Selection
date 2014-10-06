#Alexander Allan
#06/10/2014
#Selection Exercises 2-3

print("This program will tell you how much you will be getting payed this week.")
WorkHours = float(input("Please enter the amount of hours you have worked this week: "))
if WorkHours < 0 or WorkHours > 60:
    print("You work either too many hours, or not enough hours to program.")
else:
    HourlyWage = float(input("Please enter your hourly wage: £"))
    Payment = (WorkHours * HourlyWage)
    print("This week, you will be getting payed £{0}.".format(Payment))
