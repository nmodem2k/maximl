a=input("Enter the value of a")
k=[]
for i in range(0,len(a)):
  for j in range(i+1,len(a)+1):
    l=a[i:j]
    k.append(l)
uniquee=list(set(a))
o=[]
for i in k:
  for j in uniquee:
    if j not in i:
      break
  else:
    o.append(i)
min_len=len(o[0])
for i in o:
  if len(i)<min_len:
    min_len=len(i)

print(min_len)
print("Assignment of MAximl for hiring")

