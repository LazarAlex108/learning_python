
a="calabbalac"
b=len(a)
if b%2!=0:
    jum=int((b-1)/2)
    a_prim=a[:jum]
    a_ultim=a[jum+1:b]
else:
    jum=int(b/2)
    a_prim=a[:jum]
    a_ultim=a[jum:b]

print(a_prim,a_ultim)
i=0
j=1
pal=True
while i<jum and pal!=False :
  if a_prim[i]!=a_ultim[-j]:
    pal=False
    break
  i+=1
  j+=1
print(pal)
