def first_der(f,x):
    return (f(x+e) - f(x)) / e

def sec_der(f,x):
    return (first_der(f,x+e) - first_der(f,x)) / e
def newton(f,df,x0,e):
    x = x0
    while abs(x1-x0) > e:
        x1 = x0 - first_der(f,x) / sec_der(f,x)
        x = x1
    return x