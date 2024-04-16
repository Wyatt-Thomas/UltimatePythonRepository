# # ========== 2.3.1 ==========
# while True:
#     print("Hi")
#     word=input("Shall i continue") 
#     if word =="no":
#         break

# ========== 2.3.2 ==========
# from math import sqrt
# while True:
#     number=int(input("Please type in a Number"))
#     if number==0:
#         break
#     if number>0:
#         print(sqrt(number))

# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number == 0:
#     break

# print("Now!")

# ========== 2.3.4 ==========
# password=input("Password:")
# while True:
#     re=input("Repeat password")
#     if password==re:
#         print("User account created!")
#         break
#     else:
#         print("They do not match!")

# ========== 2.3.5 ==========
# num=0
# while True:
#     pin=int(input("Pin:"))
#     if pin==4321:
#         print("Correct It took you",num,"attempts")
#         num=0
#     else:
#         num=num+1
#         print("Wrong")


# ========== 2.3.6 ==========
# year=int(input("Year:"))
# year2=year+1
# while True:
#     if year%4==0:
#         year2=year+4
#         print("The next leap year after",year,"is",year2)
#         break
#     else:
#         year2=year2+1

# ========== 2.3.7 ==========
# sentence=input("Please type in a word ")
# while True:
#     word=input("Please type in a word ")
#     if word=="end":
#         print(sentence)
#         break
#     else:
#         sentence=sentence+" "+word
# ========== 2.3.8 ==========
# sentence=input("Please type in a word ")
# repeatW=sentence
# while True:
#     word=input("Please type in a word ")
#     if word=="end":
#         print(sentence)
#         break
#     if repeatW==word:
#         print(sentence)
#         break
#     else:
#         sentence=sentence+" "+word
#         repeatW=word
# ========== 2.3.9 ==========
print("Please type in integer numbers Type in 0 to finish")
number=int(input("Number:"))
positive=0
negative=0
Mean=0
Sum=0
amount=1
while True:
    if number==0:
        print("numbers typed in:",amount)
        print("Sum of numbers:",Sum)
        print("Mean of Numbers",Mean)
        print ("Positive of numbers",positive)
        print("Negative numbers",negative)

        break
    else:
        if number>positive:
            positive=positive+1
        if number<negative:
            negative=negative+1
        Sum=Sum+number
        Mean=Sum/amount
        amount=amount+1
        number=int(input("Number:"))

