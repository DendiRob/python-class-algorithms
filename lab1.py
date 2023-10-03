import math

def lab1(start, finish, step, lowerLimit, upperLimit):
    sumNegative = 0
    negativeCounter = 0
    zoneSum = 0
    startAmount = start
    for x in range(startAmount, finish + 1):
        y = startAmount**2 * math.cos(startAmount)+ math.sqrt(math.fabs(startAmount**3-startAmount**2))+math.exp(startAmount)
        if y < 0:
            sumNegative += y
            negativeCounter += 1
        if lowerLimit <= y <= upperLimit:
            zoneSum += y
        print(f"значение x = {round(startAmount,1)}, значение функции {round(y, 4)}")
        startAmount += step
    if(negativeCounter == 0):
        averageAmount = 'we dont have any negative amounts'
    else:
        averageAmount = round((sumNegative / negativeCounter),4)
    print(f"1) среднее арифмитическое: {averageAmount}, 2)сумма чисел на отрезке ({lowerLimit}; {upperLimit}) - {round(zoneSum,4)}, 3)количество всех отрицательных значений функции - {negativeCounter}")

lab1(-5, 5, 0.2, -10, 10)
