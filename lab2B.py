from random import randint
N=8
A=2
B=4
summ=0
M=2
P=10
rand_set=[randint(A,B) for i in range(N)]
print(rand_set)
i=0
first=[]
def sum_of_digits(num):
    sum = 0
    while num>0:
        sum += num % 10
        num //= 10
    return sum
while i<N:
    if M<=sum_of_digits(abs(rand_set[i]))<=P:
        first.append(rand_set[i])
    
    i+=1
print('первое задание',first)
max1=max(rand_set)
max1ind=rand_set.index(max1)
max2=A
for i in range(N):
    if max2<=rand_set[i]<max1:
        max2=rand_set[i]
if max2==max1:
    print('второе задание','номер max1',max1ind+1,'номер max2-не существует','сумма max1 и max2 не существует')
else:
    max2ind=rand_set.index(max2)
    print('второе задание','номер max1',max1ind+1,'номер max2',max2ind+1,'сумма max1 и max2',max1+max2)
chet=[]
for i in range(N):
    if rand_set[i]%2==0:
        chet.append(rand_set[i])
chet=set(chet)
print('третье задание',len(chet))
        

    
   
    

       
    
    
