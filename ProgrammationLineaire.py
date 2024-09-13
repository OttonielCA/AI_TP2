from pulp import *
import matplotlib.pyplot as plt
import numpy as np

# Initialisation du probleme
prob = LpProblem("JobHoursMaxOptim", LpMaximize)

# Variables
j1 = LpVariable("x", 0, 12)
j2 = LpVariable("y", 0, 12)

# Contraintes
prob += j1 + j2 <= 12
prob += 2 * j1 + j2 <= 16

# Fonction Objective
prob += 40 * j1 + 30 * j2

# Resolution du probleme
prob.solve(PULP_CBC_CMD(msg=False))

# Affichage des résultats
print(LpStatus[prob.status])
print(f"Optimal objective value (Z) : {prob.objective.value()}")
print(f"Value of j1: {j1.value()}")
print(f"Value of j2: {j2.value()}")

# Prend les valeurs de x et y (j1 et j2)
j1_opt = j1.value()
j2_opt = j2.value()

# Contraintes de la variable x
x = np.linspace(0, 12, 400)

# Constraint 1: x + y <= 12
y1 = 12 - x

# Constraint 2: 2x + y <= 16
y2 = 16 - 2 * x

# Plot the feasible region
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=r'$x + y \leq 12$', color='blue')
plt.plot(x, y2, label=r'$2x + y \leq 16$', color='green')

# Fill the feasible region
plt.fill_between(x, np.minimum(y1, y2), 0, where=(y1 >= 0) & (y2 >= 0), color='gray', alpha=0.3)

# Plot the axes and labels
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xlabel('j1 (x)')
plt.ylabel('j2 (y)')

# Plot the optimal solution
plt.plot(j1_opt, j2_opt, 'ro', label='Optimal Solution')
plt.text(j1_opt, j2_opt, f'  ({j1_opt}, {j2_opt})', verticalalignment='bottom')

# Add legend and title
plt.legend()
plt.title('Feasible Region and Optimal Solution')

# Display the plot
plt.grid(True)
plt.show()
