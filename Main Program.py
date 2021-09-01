s=str(input("enter a word"))
x=0
for i in range (int(len(s)/2)):
    if s[i]==s[len(s)-i-1]:
        x=x+1
    else :
        x=0
if x==int(len(s)/2):
    print("the word is a palindrome.")
else:
    print("this word is not a palindrome.")
