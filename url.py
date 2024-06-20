# url evaluation
import re
file=open('example.txt','r')
data=file.read()
pattern=re.compile(r"(http|https)://[a-z0-9.-_]+")   

res=re.finditer(pattern,data)

for row in res:
    print("valid url:",row.group())

file.close()

