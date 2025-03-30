while True:
    str1 = input("Первый список: ")
    nums1 = str1.split(' ')
    b = False

    while '' in nums1:
        nums1.remove('')
    for num in nums1:
        if not(num.isdigit()):
            b = True

    if len(nums1) == 0 or b == True:
        print("Ошибка ввода!")
    else:
        break


while True:
    str2 = input("Второй список: ")
    nums2 = str2.split(' ')
    b = False

    while '' in nums2:
        nums2.remove('')
    for num in nums2:
        if not(num.isdigit()):
            b = True

    if len(nums2) == 0 or b == True:
        print("Ошибка ввода!")
    else:
        break


s1 = set(nums1)
s2 = set(nums2)
print(f"Общие элементы: {' '.join(s1 & s2)}")