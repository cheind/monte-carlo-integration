import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Rectangle

fig, ax = plt.subplots(figsize=plt.figaspect(1))

ax.add_patch(Rectangle((0, 0), 1, 1, 0, facecolor=None, edgecolor="k", fill=False))
ax.add_patch(Arc((0, 0), 2, 2, 0, theta1=0, theta2=90))
ax.set_aspect("equal")
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
fig.savefig("docs/quadrant.svg")
plt.close()
