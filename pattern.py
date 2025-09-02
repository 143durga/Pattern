import matplotlib.pyplot as plt
import numpy as np

# Use dark background style
plt.style.use("dark_background")

# Generate t values
t = np.linspace(0, 2 * np.pi, 1500)

# Parametric equations
x = np.cos(t) * (1 - 0.6 * np.cos(20 * t))
y = np.sin(t) * (1 - 0.6 * np.cos(20 * t))

# Scatter plot
plt.scatter(x, y, c=t, cmap="spring", s=2)

# Equal axis for better shape
plt.axis("equal")
plt.show()
