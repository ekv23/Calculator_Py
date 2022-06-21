import random


numb_type = 'r'
numb_value = 0
numb_oper = '+'

def get_type(flag):
    global numb_type
    if flag == 0:
        chck = True
        while(chck): 
            chck = True
            numb_type = input('input number type (r - real, c - complex): ')
            if numb_type in ('r','c'): chck = False
    elif flag == 1: numb_type = 'r'
    elif flag == 2: numb_type = 'c'
    else: numb_type = 'invalid flag'
    return numb_type

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        print('not a real number, try again')
        return False

def is_complex(value):
    try:
        complex(value)
        return True
    except ValueError:
        print('not a real number, try again')
        return False

def get_value(flag):
    global numb_value
    if flag == 0:
        chck = True
        while(chck):
            chck = True
            if numb_type == 'r':  
                numb_value = input("real number value (using '.'') = ")
                if is_float(numb_value): chck = False
            if numb_type == 'c':  
                numb_value = input('complex number value ([Re]+[Im]j) = ')
                if is_complex(numb_value): chck = False
    elif flag == 1: numb_value = str(random.uniform(-10, 10))
    elif flag == 2: numb_value = str(complex(random.uniform(-10, 10), random.uniform(-10, 10)))[1:-1]
    return numb_value

def get_oper(flag):
    global numb_oper
    op = ['+', '-', '*', '/']
    if flag == 0:
        chck = True
        while(chck): 
            chck = True
            numb_oper = input('input operation (+, -, * or /): ')
            if numb_oper in op: chck = False
    elif flag == 1 or flag == 2: numb_oper = op[random.randint(0,3)]
    return numb_oper 

def view_res(flag, res):
    if flag == 0:
        chck = True
        while(chck): 
            chck = True
            res_path = input('output the result to (c - console, f - local file): ')
            if res_path in ('c','f'): chck = False
    else: res_path = 'f'
    if res_path == 'c': print(res)
    else: 
        with open('res.txt', 'a') as rs:
            rs.write(f'{res}\n')
    return res

def menu_collection(flag):
    return (get_type(flag), get_value(flag), get_value(flag), get_oper(flag))