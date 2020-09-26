from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
mapper = lambda arr: list(map(lambda x: float(x), arr))
with open('./points.xyz', 'r') as f:
    f.readline()
    points = [mapper(x.split()[:-1]) for x in f]

points = np.array(points)
hull = ConvexHull(points)
print(hull)
hull_indices = np.unique(hull.simplices.flat)
hull_pts = points[hull_indices, :]
print(hull_pts)
import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.plot(points[hull.vertices,0], points[hull.vertices,1], 'r--', lw=2)
plt.plot(points[hull.vertices[0],0], points[hull.vertices[0],1], 'ro')
plt.show()
# print(points)

