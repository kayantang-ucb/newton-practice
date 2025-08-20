def first_der(f,x,e):
    return (f(x+e) - f(x)) / e

def sec_der(f,x,e):
    return (first_der(f,x+e,e) - first_der(f,x,e)) / e
def newton(f,x,e = 1e-4):
    x1 = x
    x0 = 0
<<<<<<< HEAD
    while abs(x1-x0) > 1e-2:
        x1 = x0 - first_der(f,x) / sec_der(f,x)
        x0 = x1
    return x1
=======
    while abs(x1-x0) > 1e-3:
        x1 = x0 - first_der(f,x) / sec_der(f,x)
        x0 = x1
    return x1
>>>>>>> 14b98a1eeb64f17f04bbb0bb3aa8ba906fd3eb23
