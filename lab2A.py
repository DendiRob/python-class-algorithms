import random
def lab2(sizeOfList,startZone,finishZone):
    list = []
    #fill our list
    for x in range(sizeOfList):
        randomNumber = random.randint(startZone, finishZone)
        list.append(randomNumber)
    print(list)
    #1
    #checking left and right neighbours
    for index in range(len(list)):
        #checking left and right neighbours
        if(index == 0):
            print(f'{list[index]}-нет левого соседа')
        elif(index == (len(list) - 1)):
            print(f'{list[index]}-нет правого соседа')
        else:
            if(list[index - 1]<list[index]<list[index + 1]):
                print(list[index])
    minChislo = min(list)
    minCount = 0
    for i in range(len(list)):
        if list[i] == minChislo:
            minCount += 1
    print(f'наименьшее число {minChislo}')
    print(f'количество вхождений {minCount}')
    print(f'#2')
    #2
    #find amount of Elems which is bigger than the left neighbour.Find amount and sum of Elems
    #which is positive and can be divided into 3
    amountBiggerLeft = 0
    amountPositiveAndDivided=0
    sumPositiveAndDivided=0
    for index in range(len(list)):
        if(index == 0):
            print(f'{list[index]}-нет левого соседа')
        elif(list[index-1]< list[index]):
            amountBiggerLeft += 1
            if(list[index] > 0 and list[index] % 3 == 0):
                amountPositiveAndDivided += 1
                sumPositiveAndDivided += list[index]
        elif (list[index] > 0 and list[index] % 3 == 0):
            amountPositiveAndDivided += 1
            sumPositiveAndDivided += list[index]
    print(f'{amountBiggerLeft} число чисел,которые больше левого соседа')
    print(f'{sumPositiveAndDivided} сумма чисел, которые больше 0 и делятя на 3')
    print(f'{amountPositiveAndDivided} количество чисел которые больше 0 и делятся на 3')
    print(list)#просто список элементов,облегчит проверку
    print(f'#3')
    #3
    #Find amount and sum of Elems
    #which is positive and can be divided into 5 and cant into 7
    Divided5And7Arr = []
    sumDivide5and7 = 0 
    amountDivide5and7 = 0 
    for index in range(len(list)):
        if(list[index] % 5 == 0 and list[index] % 7 != 0):
            Divided5And7Arr.append(list[index])
            sumDivide5and7 += list[index]
            amountDivide5and7 += 1
    print(f'{sumDivide5and7} сумма чисел, которые делятся на 5 , но не делятся на 7')
    print(f'{amountDivide5and7} количество чисел,которые делятся на 5, но не делятся на 7')
    #вторая часть 3 задания
    reverseArr = []
    sumEvenNumbers = 0
    amountEvenNumbers = 0
    for index in range(len(list)):
        if(list[index] % 2 == 0):
            sumEvenNumbers += list[index]
            amountEvenNumbers += 1
            reverseArr.append(list[index])
    print(f'обычный массив {list}')
    print(f'реверсивный массив{reverseArr[::-1]}')
    print(len(reverseArr))

lab2(10,-100,100)
