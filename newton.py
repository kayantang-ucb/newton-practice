def first_deriv(f, x, epsilon = 1e-5):
    """
    Approximate the first derivative of a function at a given point
    f: the function to differentiate
    x: the point at which to evaluate the derivative
    epsilon: small step size for the finite difference approximation (default = 1e-5)
    """
    return (f(x + epsilon) - f(x)) / epsilon

def sec_deriv(f, x, epsilon = 1e-5):
    """
    Approximate the second derivative of a function at a given point
    f: the function to differentiate
    x: the point at which to evaluate the second derivative
    epsilon: small step size for the finite difference approximation (default = 1e-5)
    """ 
    return (first_deriv(f, x + epsilon, epsilon) - first_deriv(f, x, epsilon)) / epsilon
    
def newton(f, x0, epsilon = 1e-5, tolerance = 1e-3):
    """
    Use the Newton's method to find the local minimum of a function
    f: the function to find the minimum
    x0: starting value
    epsilon: small step size for the finite difference approximation (default = 1e-5)
    tolerance: the stopping criterion for the Newton's method (default = 1e-3)
    """ 
    x = x0
    x1 = x0 - first_deriv(f, x0, epsilon) / sec_deriv(f, x0, epsilon)
    while abs(x1 - x) > 1e-3:
        x = x1
        x1 = x0 - first_deriv(f, x0, epsilon) / sec_deriv(f, x0, epsilon)
    return x1

