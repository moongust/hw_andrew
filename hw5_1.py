__author__ = ""

# Задание-1: Дата задана в виде строки формата 'dd.mm.yyyy'. Проверить, корректно ли введена дата.
# Выполнить решение в виде функции (шаблон приведен ниже), функция возвращает True или False
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

def check_date(date_str):
    pass
