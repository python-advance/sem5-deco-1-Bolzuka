# Инвариантне задание
# 2.1 Разработать прототип программы «Калькулятор», позволяющую выполнять базовые арифметические действия и функцию обертку, сохраняющую название выполняемой операции, аргументы и результат в файл
# 2.2 Дополнение программы «Калькулятор» декоратором, сохраняющий действия, которые выполняются в файл-журнал.
# 2.3 Рефакторинг (модификация) программы с декоратором модулем functools
# 2.4 Формирование отчета по практическому заданию и публикация его в портфолио.

# Вариативное задание
# 2.3 Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции.

# Программа «Калькулятор» - это программа, позволяющая осуществлять конвертацию курса валюты, на основе информации ЦБР. Основа программы - функция (класс), принимающая число (в том числе число с плавающей точкой) и условное обозначение валюты, из которой идет преобразование и валюты, в которую преобразовывается.


import urllib.request
from xml.etree import ElementTree as ET

def logger(function):
    import functools
    import datetime
    @functools.wraps(function)
    def wrapper(in_currency):

        t = datetime.datetime.now()
        result = function(in_currency)
        t = datetime.datetime.now() - t

        with open('Record.txt', 'a') as f:
            f.write("\n")
            f.write("_" * 20)
            f.write("\n")
            f.write("Переводим " + str(in_currency) + " " + str(in_type) + " в " + str(convert_to) + "\n")
            f.write("Результат: " + str(result) + " " + str(convert_to) +"\n")
            f.write("Время выполнения декорируемой функции " +  str(t))
            f.write("\n")
        return result
    return wrapper


print ("Конвертер рублей в другую валюту")
in_currency = float(input("Введите сумму: "))
in_type = input("Введите валюту из которой переводим (rubl, dollar, euro, iena):")
convert_to = input("Введите валюту в которую переводим (rubl, dollar, euro, iena): ")

id_dollar = "R01235" #USD
id_euro = "R01239" #EUR
id_iena = "R01820" #GBP

valuta = ET.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp"))

@logger
def convert(in_currency):
  for line in valuta.findall('Valute'):
    id_v = line.get('ID')
    if id_v == id_dollar:
        rub1 = line.find('Value').text
        print (rub1)
    elif id_v == id_euro:
        rub2 = line.find('Value').text
        print (rub2)
    elif id_v == id_iena:
        rub3 = line.find('Value').text
        print (rub3)
       
  rub1 = float(rub1.replace(',', '.'))
  rub2 = float(rub2.replace(',', '.'))
  rub3 = float(rub3.replace(',', '.'))


  if in_type == "rubl":
    if convert_to == "rubl":
      result = float (in_currency)
    elif convert_to == "dollar":
      result = float (in_currency) / rub1
    elif convert_to == "euro":
      result = float (in_currency) / rub2
    elif convert_to == "iena":
      result = float (in_currency) / rub3
   
  elif in_type == "dollar":  
    if convert_to == "rubl":
      result = float (in_currency) * rub1
    elif convert_to == "dollar":
      result = float (in_currency)
    elif convert_to == "euro":
      result = (float (in_currency) * rub1) / rub2
    elif convert_to == "iena":
      result = (float (in_currency) * rub1) / rub3

  elif in_type == "euro":  
    if convert_to == "rubl":
      result = float (in_currency) * rub2
    elif convert_to == "dollar":
      result = (float (in_currency) * rub2) / rub1
    elif convert_to == "euro":
      result = float (in_currency)
    elif convert_to == "iena":
      result = (float (in_currency) * rub2) / rub3

  elif in_type == "iena":  
    if convert_to == "rubl":
      result = float (in_currency) * rub3
    elif convert_to == "dollar":
      result = (float (in_currency) * rub3) / rub1
    elif convert_to == "euro":
      result = (float (in_currency) * rub3) / rub2
    elif convert_to == "iena":
      result = float (in_currency)     
  return result

result = convert(in_currency)

print (in_currency, in_type, " = ", result, convert_to)
