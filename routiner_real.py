def calc(a,b,oper):     # метод, принимающий аргументами переменные и оператор совершаемый над ними.
    if type(a) == str: a_real = float(a)
    if type(b) == str: b_real = float(b)
    if type(a) == tuple: a_real = float(a[0])
    if type(b) == tuple: b_real = float(b[0])
    match oper:
        case '+': return a_real + b_real
        case '-': return a_real - b_real
        case '*': return a_real * b_real
        case '/':
            if float(b_real) == 0.0: print("Null. Shall. Not. Pa-a-a-ass.\nYou can't divide by zero, sorry, not on my shift.")
            else: return a_real / b_real