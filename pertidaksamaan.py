import sympy as sym

x = sym.Symbol('x')

# Define the inequality
inequality = x - 4 / x**2 - 8*x+7 > 0

# Simplify the inequality (optional)
simplified_inequality = sym.simplify(inequality)

# Analyze the inequality
solutions = sym.solve_univariate_inequality(inequality, x, relational=False)

print(inequality)
print(simplified_inequality)
print(solutions)
