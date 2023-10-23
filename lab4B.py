from random import randint
N=10
A=-100
B=100
i=0
t=0
k=0
chet_min=B
plus_min=B
one_min=B
a=[randint(A,B) for i in range(N)]
print(a)
for i in range(N):
    if a[i]%2==0 and a[i]<chet_min:
        chet_min=a[i]
print('минимальный четный эл-нт=',chet_min)
def contains_two_and_three(num):
    has_two=False
    has_three=False

    while num>0:
        digit=num%10
        if digit==2:
            has_two=True
        elif digit==3:
            has_three=True
        num=num//10
    
    return has_two and has_three
for i in range(N):
    if contains_two_and_three(abs(a[i])):
        print('содержит 2 и 3',a[i])
for i in range(N):
    if a[i]>0 and a[i]<plus_min:
        plus_min=a[i]
print('минимальный положительный эл-нт=',plus_min)
def starts_with_one(num):
    while num>=10:
        num//=10
    return num==1
for i in range(N):
    if starts_with_one(abs(a[i])):
        print('начинается с 1',a[i])

def contains_one(num):
    has_one=False

    while num>0:
        digit=num%10
        if digit==1:
            has_one=True
        num=num//10
    return has_one
for i in range(N):
    if contains_one(abs(a[i])) and a[i]<one_min:
        one_min=a[i]
if one_min==B:
     print('минимальный эл-нт содержащий цыфру 1 не существует')
else:
     print('минимальный эл-нт содержащий цыфру 1',one_min)
        

def is_prime(num):
    if num<2: 
        return False
    for i in range(2,int(num)):
        if num%i==0: 
            return False
    return True
for i in range(N):
    if is_prime(a[i]):
        print(a[i],'простое число')

        


    


    

