import numpy as np
import matplotlib.pyplot as plt


def plot_random_dots(N, scale=10, ax=None, cmap=None):
    """Plot some random dots"""
    if ax is None:
        fig, ax = plt.subplots()
    if cmap is None:
        cmap = plt.cm.viridis
    dots = np.random.randn(2, N)
    size = dots * scale
    ax.plot(*dots, s=size, cmap=cmap)
    return ax
