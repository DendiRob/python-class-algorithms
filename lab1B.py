import math as m
A=-5
B=5
h=0.5
x=A
k=0
t=0
l=0
while x<=B:
    y=x**2*m.cos(x)+m.sqrt(m.fabs(x**3-2**x))+m.exp(x)
    print(f'x={x:.1f},y={y:.4f}')
    if y<0 and m.trunc(y)%2!=0:
        k+=1
    n = abs(int(m.trunc(y)))
    count = len(str(n))
    r=int(str(n)[count-1])
    if r>3:
        t+=1
    p=m.fabs(y)-m.fabs(m.trunc(y))
    if p>0.2:
        l+=1
    x+=h
print('колличкстово отрицательных значений f имеющих не чет целую часть:'+str(k))
print('колличкстово значений f имеющих в младшем разряде целой ыасти чило>3:'+str(t))
print('колличкстово значений f имеющих дробную часть>0.2:'+str(l))
   
