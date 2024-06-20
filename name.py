# name evaluation 
import re
file=open('example.txt','r')
data=file.read()
pattern=re.compile(r"(Mrs|Mr|Ms)[. ]*[a-zA-Z ]+")

res=re.finditer(pattern,data)

for row in res:
    print(row.group())

file.close()