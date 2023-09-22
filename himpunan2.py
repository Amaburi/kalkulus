# if there's / or >= 0 symbols use this formula instead the first one

import sympy as sym

x = sym.Symbol('x')

# Change this to the numbers that the question asked
inequality_expr = (x**3 - x**2) / (x + 3) > 0

# Simplify the inequality (optional)
simplified_inequality = sym.simplify(inequality_expr)

# Analyze the inequality
inequality_solution = sym.solve_univariate_inequality(inequality_expr, x, relational=False)


print(inequality_solution)
