"""
==========================
Plot a stupid scatterplot!
==========================

This plots a scatterplot

"""

import numpy as np
import matplotlib.pyplot as plt

x, y = np.random.randn(2, 1000)
plt.scatter(x, y, c=y)

plt.show()

