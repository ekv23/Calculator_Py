import pytest
import routiner
from routiner import calc as Calc_num

#вручную вызываем в консоли по python -m pytest routiner_test.py

def test1_Calc_num():
    """Проверка сложения десятичных чисел в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '+')
    assert output == 17.7

def test2_Calc_num():
    """Проверка вычитания десятичных чисел в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '-')
    assert output == 1.00

def test3_Calc_num():
    """Проверка умножения десятичных чисел в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '*')
    assert output == 78.07249999999999

def test4_Calc_num():
    """Проверка деления десятичных чисел в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '/')
    assert output == 1.1197604790419162

def test5_Calc_num():
    """Проверка деления на ноль в `Calc_num` функции"""
    output = Calc_num('9.35', '0', '/')
    assert output == None

def test6_Calc_num():
    """Проверка деления нуля в `Calc_num` функции"""
    output = Calc_num('0', '123.5', '/')
    assert output == 0


def test7_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '1/5', '+')
    assert output == '4 4/5'
# Тест 7 не пройден.
# ValueError: could not convert string to float: '4 3/5'



def test8_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+2j', '7-4j', '+')
    assert output == (15-2j)

def test9_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+2j', '7-4j', '-')
    assert output == (1+6j)

def test10_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+j', '7-4j', '-')
    assert output == (-9+5j)

def test11_Calc_num():
    """Проверка умножения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+1j', '7-4j', '*')
    assert output == (-2+1j)*(7-4j)

def test12_Calc_num():
    """Проверка умножения в `Calc_num` функции"""
    output = Calc_num('-2+1j', '7.0', '*')
    assert output == (-2+1j)*7

def test13_Calc_num():
    """Проверка деления комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '7-4j', '/')
    assert output == (-2+2j)/(7-4j) 
    # Тест 13 не пройден. не получается получить результат, постоянно высвечивается ошибка
    # TypeError: float() argument must be a string or a real number, not 'complex'
    # Указываются строка 74 этого файла и строка 11 routiner_complex.py

def test14_Calc_num():
    """Проверка деления нуля в `Calc_num` функции"""
    output = Calc_num('0.0', '7-4j', '/')
    assert output == 0
    # Тест 14 не пройден. не получается получить результат, постоянно высвечивается ошибка
    # TypeError: float() argument must be a string or a real number, not 'complex'
    # Указываются строка 82 этого файла и строка 11 routiner_complex.py

def test15_Calc_num():
    """Проверка вычитания чисел в `Calc_num` функции"""
    output = Calc_num('0.5', '7-4j', '-')
    assert output == (-6.5+4j)