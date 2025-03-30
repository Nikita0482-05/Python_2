while True:  
    string = input("Введите строку: ")  
    words = ['']  

    for char in string:  
        if char != ' ':  
            words[-1] += char.lower()  
        else:  
            words.append('')  

    while '' in words:  
        words.remove('')  

    if len(words) == 0:  
        print("Строка не может быть пустой!")  
    else:  
        break  


word_count = {word: words.count(word) for word in words}  

 
for word in word_count:  
    print(f"{word}: {word_count[word]}")   