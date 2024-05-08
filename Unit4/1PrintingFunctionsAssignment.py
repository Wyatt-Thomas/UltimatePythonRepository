# ========== 4.1.1 ==========
def line(number, word):
    if word=="":
        print(number*"*")
    else:
        print(word[0]*number)
# line(7, "%")
# line(10, "lol")
# line(3, "")

# ========== 4.1.2 ==========
# def box_of_hashes(hashes):
#     count=0
#     while count<hashes:
#         line(10, "#")
#         count=count+1
#     print("")
# box_of_hashes(5)
# box_of_hashes(2)

# ========== 4.1.3 ==========
# def square_of_hashes(hashes):
#     count=0
#     while count<hashes:
#         line(hashes,"#")
#         count=count+1
#     print("")
# square_of_hashes(5)
# square_of_hashes(3)

# ========== 4.1.4 ==========
# def square(n,l):
#     count=0
#     while count<n:
#         line(n,l)
#         count=count+1
#     print("")
# square(5, "*")
# square(3, "o")

# ========== 4.1.5 ==========
# def triangle(n2):
#     count=1
#     while count<n2+1:
#         line(count,"#")
#         count=count+1
#     print()
# triangle(6)
# 


# ========== 4.1.6 ==========
# def shape(n1,x,n2,y):
#     count=1
#     while count<n1+1:
#         line(count,x)
#         count=count+1
#     count=0
#     while count<n2:
#         line(n1,y)
#         count=count+1

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")
# ========== 4.1.7 ==========
def spruce(n1):
    count=0
    amount=1
    left=n1-1
    print("A SPRUCE!")
    while count<n1:
        print(" "*left,"*"*amount)
        count=count+1
        amount=amount+2
        left=left-1
    print((n1-1)*" ","*")
spruce(3)
spruce(5)