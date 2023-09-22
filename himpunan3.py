# if there's "|" example |x+1|**2 + 2|x+2| >= 2 use this formula

import sympy as sym

x = sym.Symbol('x')

# Change this to the numbers that the question asked
inequality_expr = sym.Abs(2*x + 3) < sym.Abs(x + 6)

# Simplify the inequality (optional)
simplified_inequality = sym.simplify(inequality_expr)

# Analyze the inequality
inequality_solution = sym.solve_univariate_inequality(inequality_expr, x, relational=False)


print(inequality_solution)
