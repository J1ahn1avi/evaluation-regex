# mail.id evaluation  
import re
file=open('example.txt','r')
data=file.read()
# pattern=re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(ac\.in)\b") #collage domain mail id 
pattern=re.compile(r"\b[a-zA-Z0-9._%+=]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b") 

res=re.finditer(pattern,data)

for row in res:
    print(row.group())

file.close()

