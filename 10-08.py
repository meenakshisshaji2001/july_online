
s=input("enter your string;")#input string
counter=dict()#empty dictionary
for p in s:
    if p in counter:#if p element in the string
        counter[p]=counter[p]+1#p 
    else:
        counter[p]=1
print(counter)
