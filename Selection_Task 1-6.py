#Alexander Allan
#12/10/2014
#Selection Exercise 1-4

Number1 = int(input("Please enter the 1st number: "))

Number2 = int(input("Please enter the 2nd number: "))

if Number1 > Number2:
    print("{0} is larger than {1}.".format(Number1,Number2))
if Number2 > Number1:
    print("{0} is larger than {1}.".format(Number2,Number1))
else:
    print("{0} and {1} are both the same value.".format(Number1,Number2))
