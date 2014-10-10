#Alexander Allan
#10/10/2014
#Selection Statement Spot Check (2)

FirstName = input("Please enter your first name: ")
LastName = input("Please enter your last name: ")
Gender = input("Please enter your gender (M/F): ")
if Gender == "M":
    print("Mr. {0} {1}.".format(FirstName,LastName))
    if Gender == "F":
        print("Ms {0} {1}.".format(FirstName,LastName))
if Gender is not "M":
    print("Please enter an appopriate gender!")
if Gender is not "F":
    print("Please enter an appopriate gender!")
