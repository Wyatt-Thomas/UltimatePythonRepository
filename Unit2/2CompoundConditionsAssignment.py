# print("########## 2.2.1 ##########")
age=int(input("Please type in your age"))
if age>=5:
    print("Ok youre",age,"Years old")
elif age>=0 and age<=5:
    print("I suspect you cant wrtite quite yet...")
else:
    print("This muste be a mistake")
print("########## 2.2.2 ##########")
name=input("Please type in your name ")
if name=="Morty" or name=="Ferdie":
    print("I think you might be one of Mickey mouses nephews")
elif name=="Huey" or name=="Dewey" or name=="Louie":
    print("I think you might be one of Donald Ducks nephews")
else:
    print("Youre not a nephew of any character I know of")
# print("########## 2.2.3 ##########")
grade=int(input("Type in percent:"))
if grade>100 or grade<0:
    print("Grade:Impossible")
elif grade>+0 and grade<=59:
    print("Grade:F")
elif grade>=60 and grade<=69:
    print ("Grade:D")
elif grade>=70 and grade<=79:
    print ("Grade:C")
elif grade>=80 and grade<=89:
    print ("Grade:B")
elif grade>=90 and grade<=100:
    print ("Grade:A")
# # print("########## 2.2.4 ##########")
Number=int(input("Number:"))
if Number %  5 == 0 and Number % 3 == 0:
    print("FizzBuzz")
elif Number % 5 == 0:
    print("Buzz")
elif Number % 3 == 0:
    print("Fizz")
# print("########## 2.2.5 ##########")
year=int(input("Please type in a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("That year is a leep year")
        else: 
            print("This year is not leep year")
    else:
        print("That year is a leep year")
else: 
    print("That year is not a leep year")
    
# print("########## 2.2.6 ##########")
l1=input("1st letter")
l2=input("2nd letter")
l3=input("3rd letter")
if l1>l2 and l1<l3 or l1 >l3 and l1 < l2:
    print("The ltter in the middle is",l1)
elif l2>l1 and l2<l3 or l2 >l3 and l2<l1:
    print("The ltter in the middle is",l2)
elif l3>l2 and l3<l1 or l3>l1 and l1<l2:
    print("The ltter in the middle is",l3)