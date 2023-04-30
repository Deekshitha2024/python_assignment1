s = input("Enter a String : ")
s1=s.lower()
l=[]
for i in s1:
    if i not in l:
        l.append(i)
print(",".join(l))
    

     
    


