# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:34:15 2015

@author: DELL
"""
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.

    """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1] # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:,1] - c[1], vs[:,0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    return new_regions, np.asarray(new_vertices)

# make up data points

bk = xlrd.open_workbook("/Users/Dijkstraaaaa/Documents/LTE/changshu_location.csv")
#shxrange = range(bk.nsheets)
sh = bk.sheet_by_name("changshu_location")

nrows = sh.nrows

output = dict()
#output['raw'] = []
#output['crs'] = []
output['lon'] = []
output['lat'] = []
#points=[]

points=[[0 for x in range(2)] for y in range(111)]

for i in range(1,nrows):
        output['lon'].append(sh.cell(i,2).value)
        output['lat'].append(sh.cell(i,1).value)
print(output['lat'][0])

points[0][0]=output['lat'][0]
points[0][1]=output['lon'][0]
#print  points[0][1]

points = np.random.rand(111, 2)
print(points)
for k in range(111):
    points[k][0]=output['lat'][k]
    points[k][1]=output['lon'][k]

print(points)

#points = np.random.rand(15, 2)
#print points
# compute Voronoi tesselation
vor = Voronoi(points)
print(vor)
# plot
regions, vertices = voronoi_plot_2d(vor)
# print "--"
# print regions
# print "--"
# print vertices

# colorize
for region in regions:
    polygon = vertices[region]
    plt.fill(*zip(*polygon), alpha=0.6)

plt.plot(points[:,0], points[:,1], 'ko',markersize=2)
plt.xlim(vor.min_bound[0] - 0.1, vor.max_bound[0] + 0.1)
plt.ylim(vor.min_bound[1] - 0.1, vor.max_bound[1] + 0.1)

plt.show()
