def scrabble_score(word):
    s=0
    for letter in word:
        if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u" or letter=="l" or letter=="n" or letter=="s" or letter=="t" or letter=="r":
            s=s+1
        elif letter=="d" or letter=="g":
            s=s+2
        elif letter=="b" or letter=="c" or letter=="m" or letter=="p":
            s=s+3
        elif letter=="f" or letter=="h" or letter=="v" or letter=="w" or letter=="y":
            s=s+4
        elif letter=="k":
            s=s+5
        elif letter=="j" or letter=="x":
            s=s+8
        elif letter=="q" or letter=="z":
            s=s+10
    return s
print(scrabble_score("hello")) # 8
print(scrabble_score("world")) # 9
print(scrabble_score("zebra")) # 16
print(scrabble_score("xylophone")) # 24
word=input("Type in a word: ")
print(scrabble_score(word))
