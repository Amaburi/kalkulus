import sympy as sym

x = sym.Symbol('x')

example = x**2 + 2*x + 4
intergral = sym.integrate(example, x)

print(intergral)