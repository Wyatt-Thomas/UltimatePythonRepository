# ========== 3.4.1 ==========
# def seven_dwarves():
#     print("Bashful")
#     print("Doc")
#     print("Dopey")
#     print("Grumpy")
#     print("Happy")
#     print("Sleepy")
#     print("Sneezy")
# seven_dwarves()
# ========== 3.4.2 ==========
def first_character(word):
    print(word[0])


first_character('python')
first_character('yellow')
first_character('tomorrow')
first_character('heliotrope')
first_character('open')
first_character('night')

# # ========== 3.4.3 ==========
# def mean(n1,n2,n3):
#     print((n1+n2+n3)/3)
# mean(5,3,1)
# mean(10,1,1)


# ========== 3.4.4 ==========
# x=0
# text=input("text ")
# times=int(input("Times "))
# def print_many_times(text):
#     print(text)
# while True:
#     if times>x:
#         print_many_times(text)
#         x=x+1
#     else:
#         break

# ========== 3.4.5 ==========
# y=0
# x=int(input("length:"))
# def hash_squard(x):
#     print("#"*x)
# while True:
#     if x>y:
#         hash_squard(x)
#         y=y+1
#     else:
#         break

# ========== 3.4.6 ==========
# def chessboardline(x, z):
#     if x%2==0:
#         if z==0:
#             print ("10"*(x//2))
#         elif z==1:
#             print("01"*(x//2))
#     else:
#         if z==0:
#             print ("10"*(x//2) + "1")
#         elif z==1:
#             print("01"*(x//2)+ "0")
# def chessboard(x):
#     y = 0
#     z = 0
#     while True:
#         if x>y:
#             chessboardline(x, z)
#             y=y+1
#             if z==0:
#                 z=z+1
#             else:
#                 z=z-1
#         else:
#             break
# x=int(input("length:"))
# chessboard(x)

