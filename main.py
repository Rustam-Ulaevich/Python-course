# import turtle

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor('green')
# t.width(2)
# t.speed(50)
# col=('white','blue','red')
# for i in range(500):
#     t.pencolor(col[i%3])
#     t.forward(i*4)
#     t.right(121)

# turtle.done()


# print(10>3)
# print(type('long string' < 'long'))
# print(bool(1))


# print('10' > 5)
# print( int('10') > 5)
# a = 1
# b = 2.2
# print(a + b)
# a1 = True
# b1 = 2.2
# c1 = False
# print(a1 + b1)
# print(a1 + c1)


### list Списки - упорядоченная последовательность элементов
# list1 = [1, 2, 3, 4]
# list2 = [11, 1, 12, 42, 5, 4]
# print(list1)
# print(len(list1)) #длина списка
# print(list1[1]) #выбор значения
# del list1[-2] #delete element
# print(list1)
# list1.pop() #delete last element

# list2.sort() #сортировка
# print(list2)
# listWord = 'привет мир'
# print(list(listWord)) #конвертация в список
# arr = {'age': 35, 'color': 'red'}
# print(list(arr))

# print(sum(list2) / len(list2))
# my_list = [1, 2, 3, 4, 5]
# del my_list[2]
# print(my_list)


### Tuple Кортежи - упорядоченная последовательность элементов. Изменять нельзя!!!

list = (1, 2, 3)
# list2 = (2, 1, 3)
# print( list == list2)  False
# print( list[0] )       1
# print( list[-1] )      3
# list[0] = 5            TypeError  Изменять и удалять нельзя!!!
# print(type(list))      <class 'tuple'>

# stydent = ( {'age': 39}, {'money': 1500, }          в кортежах допускается изменять внутри элементы
# stydent[0]['age'] = 40
# print(stydent)

# all_list = list + list2   кортежи можно объединять

# count  метод подсчёта одинаковых элементов
# print(list.count(2))     1

# index  метод поиска элементов
# print(list.index(3))     2

# tuple  для конвертации в кортеж



### Set Наборы  -  Не упорядоченная последовательность элементов. Содержит только УНИКАЛЬНЫЕ элементы. Нет индексов у элементов

# list_set = { 1, 2, 'apple'}



# ## Range Диапазоны   -  Упорядоченная неизменяемая последовательность элементов.




