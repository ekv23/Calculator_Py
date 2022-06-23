# метод, принимающий аргументами переменные и оператор совершаемый над ними.

from fractions import Fraction
import re

def calc(a,b,oper):
    # если получили строку
    if type(a) == str and type(a) == str: 
        if a.find('/') < 0 and b.find('/') < 0:
            a_real = float(a)
            b_real = float(b)
            return operation(a_real, b_real, oper)
        else:
            if a[a.find('/') + 1] == '0' or b[b.find('/') + 1] == '0': return 'Error! Division by zero.'
            else: return parce_fraction_answer(operation_fraction(pars_fraction(a), pars_fraction(b), oper))

    # если получили кортеж
    if type(a) == tuple and type(b) == tuple: 
        a_real = float(a[0])
        b_real = float(b[0])
        return operation(a_real, b_real, oper)

# принимает два числа с плаваюшей точкой и возвращает ответ по операции
def operation (n1, n2, oper):
    match oper:
        case '+': return n1 + n2
        case '-': return n1 - n2
        case '*': return n1 * n2
        case '/':
            if float(n2) == 0.0: 
                return 'Error!!! Division by zero.'
            else: 
                return n1 / n2

# принимает на вход две дроби простого вида a/b и возвращает ответ операции над ними
def operation_fraction (n1, n2, oper):
    match oper:
        case '+': return f'{Fraction(n1).numerator * Fraction(n2).denominator + Fraction(n2).numerator * Fraction(n1).denominator}/{Fraction(n2).denominator * Fraction(n1).denominator}'
        case '-': return f'{Fraction(n1).numerator * Fraction(n2).denominator - Fraction(n2).numerator * Fraction(n1).denominator}/{Fraction(n2).denominator * Fraction(n1).denominator}'
        case '*': return f'{Fraction(n1).numerator * Fraction(n2).numerator}/{Fraction(n1).denominator * Fraction(n2).denominator}'
        case '/': return f'{Fraction(n1).numerator * Fraction(n2).denominator}/{Fraction(n2).numerator * Fraction(n1).denominator}'

# приводим к виду простой дроби вида a/b
def pars_fraction (number):
    ans_str = re.split(' |/', number)
    if len(ans_str) < 3: 
        return number
    else: 
        return f'{int(ans_str[0]) * int(ans_str[2]) + int(ans_str[1])}/{ans_str[2]}'

# выделяем в дроби целочисленную состовляющую (если есть), получаем вид    x a/b
def parce_fraction_answer (number):
    ans_str = number.split('/')

    if int(ans_str[0]) < 0: sign = '-'
    else: sign = ''

    if len(ans_str) < 2:
        return number
    elif ans_str[1] == '1':
        return f'{ans_str[0]}'
    elif ans_str[0] == '0':
        return f'{ans_str[0]}'        
    elif abs(int(ans_str[0])) == int(ans_str[1]):
        return f'{sign}1'
    elif abs(int(ans_str[0])) > int(ans_str[1]):
        int_num = abs(int(int(ans_str[0]) / int(ans_str[1])))
        return f'{sign}{int_num} {abs(int(ans_str[0])) - int_num * int(ans_str[1])}/{int(ans_str[1])}'
    else:
        return number