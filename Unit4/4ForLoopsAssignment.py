# # ========== 4.4.1 ==========
# word=input('Please type in a string: ')
# for  letter in word:
#     print(letter)
#     print("*")

# ========== 4.4.2 ==========
# positive=int(input('Please type in a positive integer: '))
# negative=(positive*-1)
# for number in range(negative,positive+1):
#     if number!=0:
#         print(number)
# ========== 4.4.3 ==========
# def list_of_stars(n1):
#     for number in n1:
#         print(number*("*"))
# list_of_stars([3,7,1,1,2])
# ========== 4.4.4 ==========
# def palindromes(word):
#     word2="" 
#     for letter in word:
#         word2=letter+word2
#     if word==word2:
#         return(True)
#     else:
#         return(False)
# y=input("Please type in a word:")
# x=palindromes(y)
# print(x)
# ========== 4.4.5 ==========
# def sum_of_positives(n1):
#     sum=0
#     for number in n1:
#         if number>0:
#             sum=sum+number
#     return(sum)
# my_list=[1,-2,3,-4,5]
# result = sum_of_positives(my_list)
# print("The result is", result)
# ========== 4.4.6 ==========
# my_list=[1,2,3,4,5]
# def even_numbers(n2):
#     new=[]
#     for number in n2:
#         if number%2==0:
#             new.append(number)
#     return(new)
# print("original", my_list)
# new_list=even_numbers(my_list)
# print("new", new_list)

# ========== 4.4.7 ==========
# def list_sum(a,b):
#     n=0
#     new=[]
#     for number in a:
#         sum=number+b[n]
#         new.append(sum)
#         n=n+1
#     return(new)
# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b)) # [8, 10, 12]

# ========== 4.4.8 ==========
def length_of_longest(wordlist):
    n=0
    for letter in wordlist:
        l=(len(letter))
        if l>n:
            n=l
    return(n)

my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = length_of_longest(my_list)
print(result)

# ========== 4.4.9 ==========
def shortest(wordlist):
    n=length_of_longest(wordlist)
    for letter in wordlist:
        l=(len(letter))
        if n>l:
            n=l
            p=letter
    return(p)

my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = shortest(my_list)
print(result)
