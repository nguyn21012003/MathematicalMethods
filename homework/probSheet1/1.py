import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(-np.pi, np.pi, 500, endpoint=False)

f = (theta**2 - np.pi**2) ** 2

print()

plt.figure()
plt.plot(theta, f)
plt.xlabel(r"$\theta$")
plt.ylabel(r"$f(\theta)$")
plt.title(r"$f(\theta) = (\theta^2 - \pi^2)^2$")
plt.grid(True)

plt.show()
