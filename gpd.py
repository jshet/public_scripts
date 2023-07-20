import geopandas 
import matplotlib.pyplot as plt

shape_file = "shape/Elev_Contour.shp"

gdf = geopandas.read_file(shape_file, crs="epsg:4326")

print(gdf.head())

fig = gdf.plot(linewidth=0.5, color='k', figsize=(11,8.5))

# minx, miny = -122.99, 48.54
# maxx, maxy = minx+0.1, miny+0.05
# fig.set_xlim(minx, maxx)
# fig.set_ylim(miny, maxy)

plt.tick_params(axis='both', labelsize=6)

fig.ticklabel_format(useOffset=False)
# fig.set_axis_off()

# plt.title("Title")
# plt.grid(True)

# plt.show()

plt.savefig("plot.svg", format="svg")