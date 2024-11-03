def grade(scoure):
    if scoure >= 90.0:
        print("A")
    elif scoure >= 80.0:
        print("B")
    elif scoure >= 70.0:
        print("C")
    elif scoure >= 60.0:
        print("D")
    else:
        print("F")
def main():
    scoure = float( input ("enter a secre: "))
    print("the grade is: " ,end="" )
    grade(scoure)
main()