# sem5-deco-1

### Инвариантне задание
#### 2.1 Разработать прототип программы «Калькулятор», позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл
#### 2.2 Дополнение программы «Калькулятор» декоратором, сохраняющий действия, которые выполняются в файл-журнал.
#### 2.3 Рефакторинг (модификация) программы с декоратором модулем functools
#### 2.4 Формирование отчета по практическому заданию и публикация его в портфолио.

### Вариативное задание
#### 2.3 Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции.

Декоратор
Здесь записываем в файл, назывем имя функции, выводим аргументы, результат и время выполнения декорируемой функции
```
def logger(function):
    import functools
    import datetime
    @functools.wraps(function)
    def wrapper(*args):
       
        if function.__name__ == 'summ':
            operation_name = "Сложение"
        elif function.__name__ == 'razn':
            operation_name = "Вычетание"
        elif function.__name__ == 'umn':
            operation_name = "Умножение"
        elif function.__name__ == 'dell':
            operation_name = "Деление"
        else:
            operation_name = "Неизвестная операция"
        
        t = datetime.datetime.now()
        result = function(*args)
        t = datetime.datetime.now() - t
        

        with open('Record.txt', 'a') as f:
            f.write("\n")
            f.write("_" * 20)
            f.write("\n")
            f.write("Функция: " + operation_name + "\n")
            f.write("Аргументы: " + str(args) + "\n")
            f.write("Результат: " + str(result) + "\n")
            f.write("Время выполнения декорируемой функции " +  str(t))
            f.write("\n")
        return result
        
    return wrapper
```

Функции для калькулятора
```
@logger
def summ(*args):
    """
    функция сложения
    """
    res = 0
    for arg in args:
        res += arg
    return res

@logger
def razn(*args):
    """
    функция разности
    """
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res -= arg
    return res

@logger
def umn(*args):
    """
    функция умножения
    """
    res = 1
    for arg in args:
        res *= arg
    return res

@logger
def dell(*args):
    """
    функция деления
    """
    args = list(args)
    res = args.pop(0)
    for arg in args:
        res /= arg
    return res
```

Калькулятор
```
@logger
def culculate():
    """
    функция для калькулятора
    """
    print('Инструкция: ')
    print('1) Введите действие, которое вы хотите использовать(номер)')
    print('2) Введите значения через пробел')
    print('3) Как только вы введете все значения напишите "end"')
    print('4) Посмотрите ответ')
    print('\n')

    word = input(' Введите номер действия: \n (1.Сложение, 2.Вычитание, 3.Умножение, 4.Деление)\n').upper()

    if word == '1':
        print('Введите слогаемые через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = summ(*arr)
        print("Ответ:", result)
    elif word == '2':
        print('Введите уменьшаемое и вычитаемые через пробел:')
        arr = input().split()
        arr = list(map(int, arr))
        result = razn(*arr)
        print("Ответ:", result)
    elif word == '3':
        print('Введите множители через пробел: ')
        arr = input().split()
        arr = list(map(int, arr))
        result = umn(*arr)
        print("Ответ:", result)
    elif word == '4':
        print('Делимое и делители:')
        arr = input().split()
        arr = list(map(int, arr))
        result = dell(*arr)
        print("Ответ:", result)
    else:
        print('Попробуйте еще раз :)')
culculate()
```

Ввод в консоли: 

![Скрин](https://github.com/python-advance/sem5-deco-1-Bolzuka/blob/master/deco.png "Скрин")


       
Вывод: [Файл Record.txt](https://github.com/python-advance/sem5-deco-1-Bolzuka/blob/master/Record.txt "Файл Record.txt" )
