print("\nThis is a program that checks if the year that you will input is a leap year or not.")

year = input("\nChoose a year :")

if  str(year[-1]) == str(0) and str(year[-2]) == str(0):

    if int(year) % 400 == 0 :
        print(str(year)+ " is a leap year !")

    else :
        print(str(year)+ " is not a leap year.")
        
else :

    if int(year) % 4 == 0 :
        print(str(year)+ " is a leap year !")

    else :
        print(str(year)+ " is not a leap year.")

