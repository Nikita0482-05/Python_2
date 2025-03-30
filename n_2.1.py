string = input("Введите числа через пробел: ")  
nums = string.split()  

while True:  
    power = input("Введите степень: ")  
    if power.isdigit():  
        power = int(power)  
        break  
    print("Ошибка: степень может быть только неотрицательным целым числом!")  

results = []  
for num in nums:  
    if (num.isdigit()) or (num.count('-') == 1 and num.lstrip('-').isdigit()):  
        results.append(str(int(num) ** power))  
    else:  
        results.append(num * power)  

print(f"Вывод: {' '.join(results)}") 