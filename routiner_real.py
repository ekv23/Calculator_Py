# метод, принимающий аргументами переменные и оператор совершаемый над ними.

from fractions import Fraction

def calc(a,b,oper):
    # если в полученной строку
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

# приводим дробь к обычному виду
def pars_fraction (number):
    number_slash_index = number.find(' ')
    frac_num = ''
    if number_slash_index > 0: int_num = ''        
    else: return number

    for i in range(number_slash_index):
        int_num += str(number[i])
    for i in range(number_slash_index + 1, len(number)):
        frac_num += str(number[i])

    return f'{Fraction(frac_num).numerator + int(int_num) * Fraction(frac_num).denominator}/{Fraction(frac_num).denominator}'

# выделяем в дроби целочисленную состовляющую (если есть)
def parce_fraction_answer (number):
    if Fraction(number).numerator > Fraction(number).denominator:
        int_num = str(int(Fraction(number).numerator / Fraction(number).denominator))
        return f'{int_num} {Fraction(number).numerator - int(int_num) * Fraction(number).denominator}/{Fraction(number).denominator}'
    elif Fraction(number).numerator * -1 > Fraction(number).denominator:
        int_num = str(int(Fraction(number).numerator / Fraction(number).denominator))
        return f'{int_num} {(Fraction(number).numerator - int(int_num) * Fraction(number).denominator) * -1}/{Fraction(number).denominator}'
    else:
        return number

print(calc('1 1/18', '2 3/4', '/'))