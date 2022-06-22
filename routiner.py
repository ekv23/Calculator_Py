import logger as lr
import viewer as vr
import routiner_real as rr
import routiner_complex as rc

def calc(first_numb, second_numb, numb_oper):
    lr.log_info()

    if vr.is_float(first_numb) and vr.is_float(second_numb): 
        first_numb = (float(first_numb),)
        second_numb = (float(second_numb),)
        return rr.calc(first_numb, second_numb, numb_oper)

    if vr.is_frac(first_numb) and vr.is_frac(second_numb):
        first_numb = str(first_numb)
        second_numb = str(second_numb)
        return rr.calc(first_numb, second_numb, numb_oper)
    
    if vr.is_complex(first_numb) and vr.is_complex(second_numb):
        first_numb = str(complex(first_numb))[1:-1]
        second_numb = str(complex(second_numb))[1:-1]
        return rc.calc(first_numb, second_numb, numb_oper)
    
    err = 'given numbers have different types or inappropriate format'
    lr.log_error(err)
    return err