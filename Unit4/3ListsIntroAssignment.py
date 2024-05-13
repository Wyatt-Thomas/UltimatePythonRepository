# ========== 4.3.1 ==========
# number_list=[1,2,3,4,5]
# while True:
#     index=int(input("Index: "))
#     if index==-1:
#         break
#     else:
#         val=int(input("New value:"))
#         number_list.pop(index)
#         number_list.insert(index,val)
#         print (number_list)
# ========== 4.3.2 ==========
# number_list=[]
# i=int(input("How many items:"))
# n=1
# while i>=n:

#     item=int(input(f"Item {n}:"))
#     number_list.append(item)
#     n=n+1
# print(number_list)
# ========== 4.3.3 ==========
# list=[]
# n=1
# while True:
#     N=input("a(d)d, (r)emove or e(x)it:")
#     if N=="d":
#         list.append(n)
#         n=n+1
#         print("the list is now",list)
#     elif N=="r":
#         list.pop((n-2))
#         n=n-1
#         print("the list is now",list)
#     elif N=="x":
#         break
#     else:
#         print("error, write d r or x")
# print("Bye!")

# ========== 4.3.4 ==========
word_list=[]
n=-1
while True:
    word=input("Word:")
    n=n+1
    if word in word_list:
        break
    word_list.append(word)
print("You typed in",n,"different words")