import pytest
import numpy as np
import newton


# Successful optimization
def test_simple_function():
    def f(x):
        return (x - 2) ** 2
    assert np.isclose(newton.newton(f, x0 = 5), 2.0)

# Unsuccessful optimization
def test_constant_function():
    def f(x):
        return 2.0 # Newton fails because the derivative is 0
    with pytest.raises(ValueError):
        newton(f, x0 = 1)

# Invalid user inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        newton("Hello", x0 = 2)
    
    