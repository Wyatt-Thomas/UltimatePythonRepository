# print("########## 2.1.1 ##########")
word=input("Please type in a word ")
if len(word)>1:
    print("There are",len(word),"letters in the word",word)
print("Thank you!")
# print("########## 2.1.2 ##########") 
number=float(input("Please type in a number"))
print("Integer part",int(number))
print("Decimal part",number-int(number))
# # print("########## 2.1.3 ##########")
age=int(input("How old are you? "))
if age>=18:
    print("You may vote")
else:
    print("you may not vote")
# print("########## 2.1.4 ##########")
number1=int(input("Please type in the first number"))
number2=int(input("Please type in the second number "))
if number1>number2:
    print("The greater number was",number1)
elif number2>number1:
    print("The greater number was",number2)
else:
    print("The numbers are equal")
# print("########## 2.1.5 ##########")
print("Person 1")
name1=input("Name:")
age1=int(input("Age:"))
print("Person 2")
name2=input("Name:")
age2=int(input("Age:"))
if age1>age2:
    print("The elder is",name1)
elif age2>age1:
    print("The greater number was",name2)
else:
    print(name1,"and",name2,"are the same age")
# print("########## 2.1.6 ##########")
word1=input("Please type in the 1st word ")
word2=input("Please type in the 2nd word ")
if word1>word2:
    print("The greater number was",word1)
elif word2>word1:
    print("The greater number was",word2)
else:
    print("you got the same word twice")