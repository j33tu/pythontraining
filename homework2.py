    
#home work 2
#s1L: John
#s2 jame
#want jjoahmne
a = 'john'
b = 'jame'
result = ""
lenth= len(a) if len(a) > len(b) else len(b)
for i in range(0,lenth):
    result = result + (a[i] + b[i])
    
print(result)