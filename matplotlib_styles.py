"""
Generate examples for all available styles in the repository

"""
import numpy as np
import matplotlib.pyplot as plt
import os

folder_in = "styles/"
folder_out = "examples/"
styles = os.listdir(folder_in)
for style in styles:
    with plt.style.context(folder_in + style):
        x = np.linspace(0, 4, 100)
        y = np.sin(np.pi*x + 1e-6)/(np.pi*x + 1e-6)
        fig = plt.figure()
        ax = plt.subplot(111)
        for cont in range(5):
            plt.plot(x, y/(cont + 1), label=cont)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        plt.legend(bbox_to_anchor=(1, 0.5))
        fname = style.replace("mplstyle", "svg")
        plt.savefig(folder_out + fname, bbox_inches="tight")
        fname = style.replace("mplstyle", "png")
        plt.savefig(folder_out + fname, bbox_inches="tight", dpi=300)
