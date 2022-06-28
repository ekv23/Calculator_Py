import pytest
from routiner import calc as Calc_num
#вручную вызываем в консоли по python -m pytest routiner_test.py

# Проверка вещественных чисел с точкой

def test1_Calc_num():
    """Проверка сложения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('6.75', '8.35', '+')
    assert output == 15.1

def test2_Calc_num():
    """Проверка сложения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '-9.35', '+')
    assert output == 0.00

def test3_Calc_num():
    """Проверка вычитания десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '-')
    assert output == 1.00

def test4_Calc_num():
    """Проверка вычитания десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '9.35', '-')
    assert output == 0.00

def test5_Calc_num():
    """Проверка умножения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('8.5', '3.61', '*')
    assert output == 30.685

def test6_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '/')
    assert output == 1.1197604790419162

def test7_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('6.2', '3.1', '/')
    assert output == 2.00

def test8_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '9.35', '/')
    assert output == 1.00

def test9_Calc_num():
    """Проверка деления на ноль в `Calc_num` функции"""
    output = Calc_num('9.35', '0', '/')
    assert output == None

def test10_Calc_num():
    """Проверка деления ноля в `Calc_num` функции"""
    output = Calc_num('0', '123.5', '/')
    assert output == 0.00



# Проверка смешанных и обыкновенных дробей

def test11_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '1/5', '+')
    assert output == '4 4/5'
# Тест 11 не пройден.
# ValueError: could not convert string to float: '4 3/5'

def test12_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '-3/5', '+')
    assert output == '4' 
    # output == 4  Результатом будет float или string?
# Тест 12 не пройден.
# AssertionError: assert 'given numbers have different types or inappropriate format' == '4'

def test13_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '2/5', '+')
    assert output == '5' # output == 5.00 или '4 5/5'
# Результатом будет float или string?
# Тест 13 не пройден.
# ValueError: could not convert string to float: '4 3/5'

def test14_Calc_num():
    """Проверка вычитания обыкновенных дробей в `Calc_num` функции"""
    output = Calc_num('13/15', '1/5', '-')
    assert output == '2/3' # сокращение дроби '10/15'
# Тест 14 не пройден.
# ValueError: could not convert string to float: '13/15'

def test15_Calc_num():
    """Проверка вычитания обыкновенных дробей в `Calc_num` функции"""
    output = Calc_num('10/15', '2/3', '-')
    assert output == '0' # или число будет сразу типа float 0.00?
# Тест 15 не пройден.
# ValueError: could not convert string to float: '10/15'

def test16_Calc_num():
    """Проверка умножения дробей в `Calc_num` функции"""
    output = Calc_num('2 3/4', '1/5', '*')
    assert output == '11/20'
# Тест 16 не пройден.
# ValueError: could not convert string to float: '2 3/4'

def test17_Calc_num():
    """Проверка умножения дробей в `Calc_num` функции"""
    output = Calc_num('2 3/4', '0/5', '*')
    assert output == '0' # или число будет сразу типа float 0.00?
# Тест 17 не пройден.
# ValueError: could not convert string to float: '2 3/4'

def test18_Calc_num():
    """Проверка деления дробей в `Calc_num` функции"""
    output = Calc_num('3/4', '1/2', '/')
    assert output == '1 1/2'
# Тест 18 не пройден.
# ValueError: could not convert string to float: '3/4'


def test19_Calc_num():
    """Проверка деления дробей в `Calc_num` функции"""
    output = Calc_num('3/4', '0/2', '/')
    assert output == None
# Тест 19 не пройден.
# ValueError: could not convert string to float: '3/4'


# Проверка комлексных чисел

def test20_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+2j', '7-4j', '+')
    assert output == (15-2j)

def test21_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+2j', '-8-4j', '+')
    assert output == (-2j)

def test22_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+4j', '-8-4j', '+')
    assert output == (0) # или число будет сразу типа float 0.00?

def test23_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+j', '7-4j', '-')
    assert output == (-9+5j)

def test24_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2-4j', '7-4j', '-')
    assert output == (-9) # или число будет сразу типа float -9.00?

def test25_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2-4j', '-2-4j', '-')
    assert output == (0) # или число будет сразу типа float 0.00?

def test26_Calc_num():
    """Проверка умножения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '7-4j', '*')
    assert output == (-2+2j)*(7-4j)

def test27_Calc_num():
    """Проверка умножения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '0j', '*')
    assert output == (0)
# Тест 27 не пройден.
# ValueError: complex() arg is a malformed string

def test28_Calc_num():
    """Проверка деления комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '7-4j', '/')
    assert output == (-2+2j)/(7-4j) 
# Тест 28 не пройден. не получается получить результат, постоянно высвечивается ошибка
# TypeError: float() argument must be a string or a real number, not 'complex'

def test29_Calc_num():
    """Проверка деления комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '-2+2j', '/')
    assert output == (1) # или число будет сразу типа float 1.00?
# Тест 29 не пройден.
# TypeError: float() argument must be a string or a real number, not 'complex'