# ========== 4.2.1 ==========

# def greatest_number(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         return n1
#     elif n2>n1 and n2>n3:
#         return n2
#     elif n3>n2 and n3>n1:
#         return n3
# n1=input("Numer1:")
# n2=input("Numer2:")
# n3=input("Numer3:")
# total=greatest_number(n1,n2,n3)
# print(total)

# ========== 4.2.2 ==========
# def same_chars(word,n1,n2):
#     if word[n1]==word[n2]:
#         return "True"
#     else:
#         return "False"
# T=same_chars("Programmer",6,7)
# print(T)

# ========== 4.2.3 ==========
sentence=input("Type A Sentence:")

def first_word(sentence):
    n=0
    s=""
    while True:
        if sentence[n]==" ":
            break
        else:
            s=s+sentence[n]
            n=n+1
    return(s)

first=first_word(sentence)


def second_word(sentence):
    n=0
    s=""
    while True:
        if sentence[n]==" ":
            if s==first:
                n=n+1
                s=""
            else:
                break
        else:
                s=s+sentence[n]
                n=n+1
    return(s)


def last_word(sentence):
    n=int(len(sentence)-1)
    s=""
    while True:
        if sentence[n]==" ":
            break
        else:
            s=sentence[n]+s
            n=n-1
    return(s)


print(first_word(sentence))
print(second_word(sentence)) 
print(last_word(sentence)) 