# ========== 3.3.1 ==========
# original=input("Please type in a string: ")
# n=1
# p=0
# while True:
#     if p<len(original):
#         slice=original[:n]
#         n+=1
#         p+=1
#         print(slice)
#     else:
#         break
# ========== 3.3.2 ==========
# original=input("Please type in a string: ")
# n=len(original)-1
# p=0
# while True:
#     if p<len(original):
#         slice=original[n:]
#         n-=1
#         p+=1
#         print(slice)
#     else:
#         break

# ========== 3.3.3 ==========
# word=input("Please type in a string ")
# a=("a"in word)
# if a==True:
#     print("A found")
# else:
#     print("a not found")
# e=("e"in word)
# if e==True:
#     print("e found")
# else:
#     print("a not found")
# o=("o"in word)
# if o==True:
#     print("o found")
# else:
#     print("o not found")
# ========== 3.3.4 ==========
# word=input("Please type in a word ")
# char=input("Please type in a character ")
# p=(word.find(char))
# if p+3>len(word):
#     print("")
# else:
#     print(word[p:p+3])

# ========== 3.3.5 ==========
# word=input("Please type in a word ")
# char=input("Please type in a character ")
# while True:
#     found_pos = word.find(char)
#     if found_pos==-1:
#         break
#     if len(word) < 3:
#         break
#     else:
#         print(word[found_pos:found_pos+3])
#         word=word[found_pos+1:]


# 0 1 2 3 4 5 6
# m a m m o t h

# ========== 3.3.6 ==========
# word=input("Please type in a string: ")
# substr=input('Please type in a substring;')

# found_pos=word.find(substr)
# num=found_pos

# word=word[found_pos+1:]
# found_pos=word.find(substr)

# if found_pos==-1:
#     print("The substring does not occure twice in the string")
# else:
#     num=num+found_pos
#     print("The second occurence of the substring is at index",num+1)