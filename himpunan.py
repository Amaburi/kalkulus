# if there's just a plain himpunan like 2x - 6 < 6x +4 "Lt" is less than "Gt" is greater than

import sympy as sp

# Define the Symbol
x = sp.symbols('x')

# Define the inequality
inequality = sp.Lt(2*x - 6, 6*x + 4)

# Find the HP( Himpunan penyelesaian)
solution = sp.solve(inequality, x)

# Print the HP (Himpunan penyelesaian)
print(solution)