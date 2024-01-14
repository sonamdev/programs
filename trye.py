import re
s="A man, a plan, a canal: Panama"
#s.replace(" ","")

s = re.sub('[\W_]+','',s)
s=s.lower()
print(s)
if(s.isalnum()):
        s1=s[::-1]
        if(s==s1):
            print("Palindrome")