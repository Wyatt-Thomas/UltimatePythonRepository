fn=input("Please Type in your First Name ")
Ln=input("Please Type in your last Name ")
GPA=input("Please type in your GPA ")
if Ln[0]<"L":
    hs="Monday and Thursday"
else:
    hs="Tuesday and Friday"
if GPA >str(3.86):
    S="$16000"
elif GPA>str(3.7) and GPA<str(3.86):
    S="$12000"
elif GPA>str(3.5) and GPA<str(3.7):
    S="$8000"
elif GPA>str(3.25) and GPA<str(3.5):
    S="$4000"
else:
    S="$0"
print("Hello",fn,"You should report to school on",hs+". You are eligibile for a scholarship of",S,".")