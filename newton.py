def first_der(f,x,e):
    return (f(x+e) - f(x)) / e

def sec_der(f,x,e):
    return (first_der(f,x+e,e) - first_der(f,x,e)) / e
    
def newton(f,x,e = 1e-4):
    x0 = x
    x1 = x0 - first_der(f,x0,e) / sec_der(f,x0,e)
    while abs(x1 - x0) > 1e-3:
        x0 = x1
        x1 = x0 - first_der(f,x0,e) / sec_der(f,x0,e)
    return x1

