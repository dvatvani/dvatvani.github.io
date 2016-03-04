import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

r = np.arange(0, 1., .1)
theta = np.random.rand(10)
plt.subplot(111, projection='polar')
pal = sns.color_palette('viridis', len(r))
plt.barh(r + 0.40,
         theta + 1,
         left=theta * 2 * np.pi,
         color = pal[::-1],
         linewidth=1,
         height=0.10,
         alpha=1.0)
plt.gca().set_rmax(1.41)
plt.grid(False, alpha=0.2, color='#CCCCCC', linewidth=3.0)
plt.gca().set_axis_bgcolor((1, 1, 1, .1))

xloc, xtt = plt.xticks()
yloc, ytt = plt.yticks()
plt.xticks(xloc, [])
plt.yticks(yloc[::2], [])

plt.gcf().set_size_inches(5, 5)
plt.gcf().tight_layout()
plt.gcf().savefig('radial_barh.png', facecolor=(0, 0, 0, 0))