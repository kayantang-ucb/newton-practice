import numpy as np
from numdifftools as nd

def grad(f, x):
    """ Compute the gradient of a multivariate function
    f: the multivariate function
    x: the array of points at which to evaluate the gradient
    """
    grad = nd.Gradient(f)
    return grad(x)

def hess(f, x):
    """ Compute the hessian matrix of a multivariate function
    f: the multivariate function
    x: the array of points at which to evaluate the Hessian
    """
    hess = nd.Hessian(f)
    return hess(x) 

def multivar_newton(f, x0, tolerance = 1e-3):
    """ Multivariate Newton's method to find the local minimum of a function
    f: the multivariate function
    x: the array of points
    tolerance: convergence tolerance (default = 1e-3)
    """
    x = np.asarray(x0, dtype = float)

    while True:
        g = grad(f, x)
        h = hess(f, x)
        step = np.linalg.solve(h, g)
        x_new = x - step

        if np.linalg.norm(step) < tol:
            return x_new
            
        x = x_new