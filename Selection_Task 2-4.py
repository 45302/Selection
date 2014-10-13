#Alexander Allan
#12/10/2014
#Selection Exercise 2-4

Grade = int(input("Please enter the amount of marks you got: "))

if Grade >=0 and Grade <= 40:
    print("You got a U grade if you got {0} marks.".format(Grade))

if Grade >= 41 and Grade <= 50:
    print("You got a E grade if you got {0} marks.".format(Grade))

if Grade >= 51 and Grade <= 60:
    print("You got a D grade if you got {0} marks.".format(Grade))

if Grade >= 61 and Grade <= 70:
    print("You got a C grade if you got {0} marks.".format(Grade))

if Grade >= 71 and Grade <= 80:
    print("You got a B grade if you got {0} marks.".format(Grade))

if Grade >= 81 and Grade <= 100:
    print("You got a A grade if you got {0} marks.".format(Grade))
