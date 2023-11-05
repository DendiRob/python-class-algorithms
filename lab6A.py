import random
#сортируем массив от малого к большему
def quickSort(arr):
    
    if len(arr) <= 1: # так как здесь рекурсия,то новый массив,длина которого меньше или равно 1,уже отсортирован, его последняя часть
        return arr
    
    mainElem = arr[len(arr) // 2]  # Выбираем main элемент(разделяя array на две части)
    leftArr = [x for x in arr if x < mainElem] #  элементы меньше main(левая часть)
    middleArr = [x for x in arr if x == mainElem]# элементы равные main(это те элементы или элемент,от которого началось деление)
    rightArr = [x for x in arr if x > mainElem]# элементы больше main(правая часть)
    
    return quickSort(leftArr) + middleArr + quickSort(rightArr)
#находим ключ
def findKey(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            print(f'index {i} number {arr[i]}')
    return print('finish')

        
def lab5(sizeOfList,startZone,finishZone):
    list = []
    #fill our list
    for x in range(sizeOfList):
        randomNumber = random.randint(startZone, finishZone)
        list.append(randomNumber)
    print(list)
    #sorting
    print(quickSort(list))
    #find key
    findKey(list,5)
    

lab5(10,0,10)