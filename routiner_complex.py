def calc(a,b,oper):
    if type(a) == str: a_complex = complex(a.replace(' ', ''))
    if type(b) == str: b_complex = complex(b.replace(' ', ''))
    if type(a) == tuple: a_complex = complex(str(a[0]) + '+' + str(a[1])) 
    if type(b) == tuple: b_complex = complex(str(b[0]) + '+' + str(b[1]))
    match oper:
        case '+': return a_complex + b_complex
        case '-': return a_complex - b_complex
        case '*': return a_complex * b_complex
        case '/': 
            if float(b_complex) == 0.0: print("Null. Shall. Not. Pa-a-a-ass.\nYou can't divide by zero, sorry, not on my shift.")
            else: return a_complex / b_complex