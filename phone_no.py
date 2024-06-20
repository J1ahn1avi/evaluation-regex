# phone.no evaluation
import re
file=open('example.txt','r')
data=file.read()
pattern=re.compile(r"\b\d{5}\*\d{5}\b|\b\d{10}\b|\b\d{5}\-\d{5}\b")

res= re.finditer(pattern,data)

for row in res:
    print(row.group())

file.close()

