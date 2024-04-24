# # ========== 3.2.1 ==========
# word=input('Please type in a string')
# n=int(input("Please type in an amount"))
# print(word*n)
# ========== 3.2.2 ==========
# word1=input("Please type in string 1  ")
# word2=input("Please type in string 2  ")
# len1=len(word1)
# len2=len(word2)

# if len1>len2:
#     print (word1,"Is longer")
# elif len1==len2:
#     print ("The Strings are Equally Long")
# else:
#     print (word2,"Is longer")
# ========== 3.2.3 ==========
# word=input("Please Type in a String: ")
# starting=len(word)-1
# limiter=0
# while True:
#     if starting>=-1:
#         limiter=limiter+1
#         if limiter==len(word)+1:
#             break
#         else:
#             print (word[starting])
#             starting=starting-1    
#     else:
#         break
# ========== 3.2.4 ==========
# word=input("Please type in a string: ")
# if word[1]==word[-2]:
#     print("The second and the second to last letter characters are",word[1])
# else:
#     print("The second and the second to last characters are different")

# ========== 3.2.5 ==========
# word=int(input("Width"))
# print("#"*word)

# ========== 3.2.6 ==========
# width=int(input("Width"))
# hight=int(input("hight"))
# limit=0
# while True:
#     if limit<hight:
#         print("#"*width)
#         limit += 1
#     else:
#         break

# ========== 3.2.7 ==========
word = input("Please type in a string ")
while True:
    if len(word)>0:
        print(word)
        numletters = len(word)
        print("-" * numletters)
        word = input("Please type in a string ")
    else:
        break

# # ========== 3.2.8 ==========
# word=input("Please type in a string ")
# lengh=20-len(word)
# if len(word)<20:
#     print(("*"*lengh)+word)


# # ========== 3.2.9 ==========
# word=input("Word ")
# length=int(((30-len(word))/2))-1
# print("*"*30)
# if len(word)%2==0:
#     print("*"+(" "*length)+word+(" "*length)+"*")
# else:
#     print("*"+(" "*length)+word+(" "*(length+1))+"*")
# print("*"*30)
