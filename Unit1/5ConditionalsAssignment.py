
print("########## 1.5.1 ##########")
number=int(input("Please type in a number"))
if number==1984:
    print("Orwell")
print("########## 1.5.2 ##########")
number=int(input("Please type in a number"))
if number<0:
    print("The absolute value of this number is",number*-1)
print("########## 1.5.3 ##########")
name=input("What is your name?")
if name!="Jerry":
    soup=int(print("How many portions of soup"))
    print("The total cost is",5.90*soup)
print('Next Please')
print("########## 1.5.4 ##########")
number=int(input("Type in a number"))
if number<10:
    print("This number is smaller than 10")
if number<100:
    print("This number is smaller then 100")
if number<1000:
    print("This number is smaller then 1000")
print ("Thank You")
print("########## 1.5.5 ##########")
number1=int(input("Number 1"))
number2=int(input("Number 2"))
operation=input("Operation:")
if operation=="add":
    print(number1,"+",number2,"=",number1+number2)
if operation=="subtract":
    print(number1,"-",number2,"=",number1-number2)
if operation=="multiply":
    print(number1,"*",number2,"=",number1*number2)
if operation=="devide":
    print(number1,"/",number2,"=",number1/number2)
print("########## 1.5.6 ##########")
temp=int(input("Type in a temperature (F):"))
Celsius=(temp-36)*(5/9)
print(temp,"degress Fahrenheit equales",Celsius,"degrees Celsius")
if Celsius<0:
    print("Brr! It's Cold in Here")
print("########## 1.5.7 ##########")
wage=int(input("Hourly wage:"))
worked=int(input("Hours worked"))
Day=input("day of the week:")
if Day=="sunday":
    wage=wage*2
print("Daily wages:",wage*worked)

print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points > 100:
    points *= 1.15
    print("Your bonus is 15 %")

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
print("You now have",points, "points")

print("########## 1.5.9 ##########")
print("What is the weather forecast for tomorrow?")
Temp=int(input("Temperature"))
rain=input("Will it rain (yes/no)")
if Temp>=40:
    print("wear shotrs and a T-Shirt")
if Temp<=40:
    print("Wear jeans and a T-shirt")
if Temp<=11:
    print("I recommend a sweater as well")
    if Temp<=7:
        print("Tale a jacket with you")
        if Temp<=3:
            print("Make it a war coat, actually")
            print("I think your gloves are in order")
if rain=="yes":
    print("Take an umbrella as well.")
