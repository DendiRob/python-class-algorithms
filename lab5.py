import random
#сортируем массив от малого к большему
def bubbleSort(arr):
    arrRange = len(arr)
    for i in range(arrRange):
        if(i == 0):
            for j in range(arrRange - 1):
                        if arr[j] > arr[j + 1]: 
                            arr[j], arr[j + 1] = arr[j + 1], arr[j] #двигает элемент,и так как самый большой уже в конце,то смысла делать ещё итер нет
        else:
            for j in range(arrRange - i):
                    if arr[j] > arr[j + 1]: 
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#находим ключ
def findKey(arr, key):
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            print(f'index {i} number {arr[i]}')
    return print('finish')


def vstavkiSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # берем 2ой элемент
        j = i -  1
        #проверяем является ли элемент до нынешнего больше
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # если так, то заменяем его (здесь key это (arr[j + 1])) на элемент позади (arr[j])
            j -= 1 #убавляем до -1 индекса,чтобы обращаться к тому же элементу,но только теперь он на позиции ниже
            
        arr[j + 1] = key #взависимости от исхода присваеваем элементу кей
    return arr   
        
def lab5(sizeOfList,startZone,finishZone):
    list = []
    #fill our list
    for x in range(sizeOfList):
        randomNumber = random.randint(startZone, finishZone)
        list.append(randomNumber)
    print(list)
    #sorting
    vstavkiSort(list)
    print(list)
    #find key
    findKey(list,5)
    

lab5(10,0,10)


#другой метод

