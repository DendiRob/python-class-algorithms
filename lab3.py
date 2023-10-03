import math

def lab3(a,b,h):
    amountOfFirstZone = 0
    amountOfSecondZone = 0
    amountOfThirdZone = 0
    
    x = a
    while x <= b:
        # иногда выводит -0.0 так как стоит форматирование после самого аргумента
        y = x + 0.5
        print(f"Значение аргумента: {round(x, 4)}, Значение функций: {round(y, 4)}")
        if(x**2 + y**2 <= 1 and x > 0 and y > 0):
            print('Я вхожу в первую область')
            amountOfFirstZone += 1
        if((x**2 + y**2 <= 1 and x <= 0) or (x**2 + y**2 <= 1 and x >= 0 and y < 0)):
            print('Я вхожу во вторую область')
            amountOfSecondZone += 1
        if((x**2 + y**2 <= 1 and y > 0) or (x < 0 and y <= 0)):
            print('Я вхожу в третью область')
            amountOfThirdZone += 1
        x += h
    print(f"Количество вхождений в первую область: {amountOfFirstZone}")
    print(f"Количество вхождений во вторую область: {amountOfSecondZone}")
    print(f"Количество вхождений в третью область: {amountOfThirdZone}")

lab3(-1,1,0.1)
    