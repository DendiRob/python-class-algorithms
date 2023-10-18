import random
def findMinAmount(array):
    minChislo = array[0]
    for i in array:
        if i <= minChislo:
            minChislo = i
    return minChislo

def findMaxAmount(array):
    maxChislo = array[0]
    for i in array:
        if i > maxChislo:
            maxChislo = i
    return maxChislo
def leftShift(array):
    firstElemIndex = 0
    shiftedArr = []
    for i in range(len(array)):
        if(i != firstElemIndex):
            shiftedArr.append(array[i])
    shiftedArr.append(array[firstElemIndex])
    return shiftedArr

def lab2(sizeOfList,startZone,finishZone):
    list = []
    #заполняем массив 
    for x in range(sizeOfList):
        randomNumber = random.randint(startZone, finishZone)
        list.append(randomNumber)
    print(list) #array
    
    maxChislo = findMaxAmount(list)
    print(f'maxChislo: {maxChislo}')
    minChislo = findMinAmount(list)
    print(f'minChislo: {minChislo}')
    sumMinMax = minChislo + maxChislo
    print(f'sumOfMinMax: {sumMinMax}')
    # A1 заменяем все отрицательные числа на сумму мин и макс
    indexElemA1 = 0
    arrA1 = []
    for i in list:
        if(i < 0):
            arrA1.append(sumMinMax)
            indexElemA1 += 1
        else:
            arrA1.append(i)
            indexElemA1 += 1
    print(f'{arrA1}-измененный массив A1') #changed array
    #A2 
    indexElemA2 = 0
    arrA2 = []
    for i in list:
        if((i % 5 == 0) and (i % 7 != 0)):
            arrA2.append(maxChislo)
            indexElemA2 += 1
        else:
            arrA2.append(i)
            indexElemA2 += 1
    print(f'{arrA2}-измененный массив A2') #changed array
    #A3
    shiftedArrA3 = leftShift(list)
    print(f'{shiftedArrA3}-сдвинулся на одну позицию влево A3')
    print(f'{findMinAmount(shiftedArrA3)} минимальное число массиваA3')
lab2(10,-100,100)


#Вводить числа с клавиатуры
def lab2Keyboard(sizeOfList):
    list = []
    #заполняем массив 
    for x in range(sizeOfList):
        number = int(input())
        list.append(number)
    print(list) #array
    
    maxChislo = findMaxAmount(list)
    print(f'maxChislo: {maxChislo}')
    minChislo = findMinAmount(list)
    print(f'minChislo: {minChislo}')
    sumMinMax = minChislo + maxChislo
    print(f'sumOfMinMax: {sumMinMax}')
    # A1 заменяем все отрицательные числа на сумму мин и макс
    indexElemA1 = 0
    arrA1 = []
    for i in list:
        if(i < 0):
            arrA1.append(sumMinMax)
            indexElemA1 += 1
        else:
            arrA1.append(i)
            indexElemA1 += 1
    print(f'{arrA1}-измененный массив A1') #changed array
    #A2 
    indexElemA2 = 0
    arrA2 = []
    for i in list:
        if((i % 5 == 0) and (i % 7 != 0)):
            arrA2.append(maxChislo)
            indexElemA2 += 1
        else:
            arrA2.append(i)
            indexElemA2 += 1
    print(f'{arrA2}-измененный массив A2') #changed array
    #A3
    shiftedArrA3 = leftShift(list)
    print(f'{shiftedArrA3}-сдвинулся на одну позицию влево A3')
    print(f'{findMinAmount(shiftedArrA3)} минимальное число массиваA3')
#lab2Keyboard(10)
