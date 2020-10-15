def test1(array1):
    #result = []
    #array1.sort()
    #result = array1[-2]
    #print(result)
    
    
    y = max(array1)
    array1.remove(y)
    new_list = []
    for value in array1:
        new_list.append(value)
        for i in new_list:
            result = max(new_list)
        
    print(result)
test1([4, 7, 36, 46, 6])


def test2(array2):
    result = []
    array2.sort()
    second_max = array2[-2]
    second_min = array2[1]
    result = second_max + second_min
  
    print(result)


# Пример ниже должен вывести 42, потому что (36 + 6)
test2([4, 7, 36, 46, 6])


def test3(array3, array4):
    result = []
    for i in range(len(array3)):
        result.append(array3[i] + array4[i])
    
    # Создать и напечатать новый массив, элементы которого равны суммам элеметов массивов array3 и array4
    print(result)


# Пример ниже должен вывести [5, 7, 9]
test3([1, 2, 3], [4, 5, 6])



# есть словарь Примеры ниже. Если в словаре нет поля name, вывести "имя не задано". Если есть имя и sex,
# вывести 'Lisa is a girl' или 'Slava is a boy, где имя берется из ключа name, а girl или boy определяются ключем sex'
# Если sex не задан либо не соответсвует этим двум значением, вывесли "Vasya is someone", где имя берется из ключа name

dict1 = {
    'name': 'Slava',
    'sex': 'male'
}
dict2 = {
    'name': 'Lisa',
    'sex': 'female'
}
dict3 = {
    'name': 'Vasiliy',
    'sex': 'abs'
}
dict4 = {
    'age': '33',
    'sex': 'abs'
}
dict5 = {
    'name': 'Ivanka',
    'sex': 'abs'
}


def test4(mydict):
    result = ''
    

    def create_text():
        if "name" not in mydict:
            return "имя не задано"
        if "male" in mydict.values():
            return "{} is a boy".format(mydict["name"])
        if "female" in mydict.values():
            return "{} is a girl".format(mydict["name"])
        if "female" or "male" not in mydict.values():
            return "{} is someone".format(mydict["name"])
        
    result = create_text()

                
    print(result)
    
            

# Задание выше
test4(dict1)
test4(dict2)
test4(dict3)
test4(dict4)
test4(dict5)
