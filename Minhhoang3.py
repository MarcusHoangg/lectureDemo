'''''
money =float(input("enter your money : "))
if money >=5:
    print("you can buy latte")
'''


#ex3
''''
age = int(input("enter your age : "))
if age >= 18 :
    print("the medicine can be administered")
if 15<=age<18 :
    weight=float(input("enter your weight : "))
    if 15<=age<=20 and weight>=55:
        print("the medicines can be used")
    else:
        print("the medicines can not be used")
'''

#ex3
'''
score =int(input("enter your score : "))
if score >= 90:
    print("you are A1")
elif score >= 80:
    print("you are A2")
elif score >= 70:
    print("you are B1")
elif score >= 60:
    print("you are B2")
elif score >= 50:
    print("you are C1")
elif score >= 40:
    print("you are C2")
else :
    print("you are fail")
'''
#HOMEWORK
#ex1
'''
length = int(input("enter zander length : "))
if length <42 :
    print("release the fish back into the lakes ")
    centimeters = 42-length
    print("your fish need",centimeters," centmeters to meet the size gap")
elif length >=42 :
    print("you can take the fish")
'''
#ex2
'''
Cabin = str(input("enter your cabin class  : "))
if Cabin == "lux":
    print("upper-desk cabin with a balcony")
elif Cabin == "A":
    print("above the car deck,equipped with a window")
elif Cabin == "B":
    print("windowless cabin above the car ")
elif Cabin == "C":
    print("windowless cabin below the car ")
else:
    print("invalid cabin class")
'''
#ex3
'''
gender = str(input("enter your biological gender : "))
hemoglobin = int(input("enter your hemoglobin : "))
if gender == "male":
    if 117<=hemoglobin:
        print("you value low")
    elif hemoglobin >=155:
        print("you value high")
    else :
        print ("you are normal")
if gender == "female":
    if 134<=hemoglobin:
        print("you value low")
    elif hemoglobin >=167:
        print("you value high")
    else :
        print ("you are normal")
'''
#ex4
'''
year=int(input("enter your year : "))
if year %4 ==0 and year%100 !=0 :
    print("your year is a leap year")
elif year%100 == 0 and year%400 ==0 :
    print("your year is a leap year")
else:
    print("your year is not a leap year")
'''



















