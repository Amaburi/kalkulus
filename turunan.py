import sympy as sym

x = sym.Symbol('x');
# adjust it to the asked question
inequality = sym.Lt(2*x - 6, 6*x + 4)
x_example = sym.diff(inequality, x)
print(x_example)
print(inequality)