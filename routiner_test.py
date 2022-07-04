import pytest
from routiner import calc as Calc_num
#вручную вызываем в консоли по python -m pytest routiner_test.py

# Проверка вещественных чисел с точкой

def test1_Calc_num():
    """Проверка сложения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('6.75', '8.35', '+')
    assert output == '15.1'

def test2_Calc_num():
    """Проверка сложения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('-6.75', '8.35', '+')
    assert output == '1.6'

def test3_Calc_num():
    """Проверка сложения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('-9.75', '8.35', '+')
    assert output == '-1.4'

def test4_Calc_num():
    """Проверка сложения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '-9.35', '+')
    assert output == '0.0'

def test5_Calc_num():
    """Проверка вычитания десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '-')
    assert output == '1.0'

def test6_Calc_num():
    """Проверка вычитания десятичных дробей в `Calc_num` функции"""
    output = Calc_num('-9.35', '8.35', '-')
    assert output == '-17.7'

def test7_Calc_num():
    """Проверка вычитания десятичных дробей в `Calc_num` функции"""
    output = Calc_num('-9.35', '-8.35', '-')
    assert output == '-1.0'

def test8_Calc_num():
    """Проверка вычитания десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '9.35', '-')
    assert output == '0.0'

def test9_Calc_num():
    """Проверка умножения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('8.5', '3.61', '*')
    assert output == '30.68'

def test10_Calc_num():
    """Проверка умножения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('3.5', '-3.1', '*')
    assert output == '-10.8'

def test11_Calc_num():
    """Проверка умножения десятичных дробей в `Calc_num` функции"""
    output = Calc_num('-3.5', '-3.1', '*')
    assert output == '10.8'

def test12_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '8.35', '/')
    assert output == '1.12'

def test13_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '-8.35', '/')
    assert output == '-1.12'

def test14_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('6.2', '3.1', '/')
    assert output == '2.0'

def test15_Calc_num():
    """Проверка деления десятичных дробей в `Calc_num` функции"""
    output = Calc_num('9.35', '9.35', '/')
    assert output == '1.0'

def test16_Calc_num():
    """Проверка деления на ноль в `Calc_num` функции"""
    output = Calc_num('9.35', '0', '/')
    assert output == 'Division by zero'

def test17_Calc_num():
    """Проверка деления ноля в `Calc_num` функции"""
    output = Calc_num('0', '123.5', '/')
    assert output == '0.0'



# Проверка смешанных и обыкновенных дробей

def test18_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '1/5', '+')
    assert output == '4 4/5'

def test19_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '-3/5', '+')
    assert output == '4' 

def test20_Calc_num():
    """Проверка сложения смешанных дробей в `Calc_num` функции"""
    output = Calc_num('4 3/5', '2/5', '+')
    assert output == '5' 

def test21_Calc_num():
    """Проверка вычитания обыкновенных дробей в `Calc_num` функции"""
    output = Calc_num('13/15', '1/5', '-')
    assert output == '2.0/3.0'

def test22_Calc_num():
    """Проверка вычитания обыкновенных дробей в `Calc_num` функции"""
    output = Calc_num('-13/15', '1/5', '-')
    assert output == '-1 1/15'

def test23_Calc_num():
    """Проверка вычитания обыкновенных дробей в `Calc_num` функции"""
    output = Calc_num('10/15', '2/3', '-')
    assert output == '0'

def test24_Calc_num():
    """Проверка умножения дробей в `Calc_num` функции"""
    output = Calc_num('2 3/4', '1/5', '*')
    assert output == '11.0/20.0'

def test25_Calc_num():
    """Проверка умножения дробей в `Calc_num` функции"""
    output = Calc_num('2 3/4', '4/5', '*')
    assert output == '2 1/5'

def test26_Calc_num():
    """Проверка умножения дробей в `Calc_num` функции"""
    output = Calc_num('2 3/4', '0/5', '*')
    assert output == '0'

def test27_Calc_num():
    """Проверка деления дробей в `Calc_num` функции"""
    output = Calc_num('3/4', '1/2', '/')
    assert output == '1 1/2'

def test28_Calc_num():
    """Проверка деления дробей в `Calc_num` функции"""
    output = Calc_num('2/5', '2/5', '/')
    assert output == '1'

def test29_Calc_num():
    """Проверка деления дробей в `Calc_num` функции"""
    output = Calc_num('3/4', '0/2', '/')
    assert output == 'Division by zero'


# Проверка комлексных чисел

def test30_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+2j', '7-4j', '+')
    assert output == '(15-2j)'

def test31_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+2j', '-8-4j', '+')
    assert output == '-2j'

def test32_Calc_num():
    """Проверка сложения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('8+4j', '-8-4j', '+')
    assert output == '0j'

def test33_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+j', '7-4j', '-')
    assert output == '(-9+5j)'

def test34_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2-4j', '7-4j', '-')
    assert output == '(-9+0j)'

def test35_Calc_num():
    """Проверка вычитания комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2-4j', '-2-4j', '-')
    assert output == '0j'

def test36_Calc_num():
    """Проверка умножения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '7-4j', '*')
    assert output == '(-6+22j)'

def test37_Calc_num():
    """Проверка умножения комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', 'j', '*')
    assert output == '(-2-2j)'

def test38_Calc_num():
    """Проверка деления комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '7-4j', '/')
    assert output == '(-0.3384615384615385+0.09230769230769233j)'

def test39_Calc_num():
    """Проверка деления комплексных чисел в `Calc_num` функции"""
    output = Calc_num('-2+2j', '-2+2j', '/')
    assert output == '(1-0j)'

def test40_Calc_num():
    """Проверка деления комплексных чисел в `Calc_num` функции"""
    output = Calc_num('3+4j', '-5+2j', '/')
    assert output == '(-0.24137931034482757-0.896551724137931j)'