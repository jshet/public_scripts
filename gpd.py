import geopandas 
import matplotlib.pyplot as plt

# read a shapefile as a geopandas dataframe using the unprojected geo coordinate system (crs)
shape_file = "shape/Elev_Contour.shp"
gdf = geopandas.read_file(shape_file, crs="epsg:4326") 

print(gdf.head()) # have a look at the data
print(gdf.bounds) # print the lat/lon bounds of the geodataframe

fig = gdf.plot(linewidth=0.5, color='k', figsize=(11,8.5)) # make the lines thin and black, set the fig w=11in and h=8.5in

# set the bounds for what data to show
minx, miny = -123.0147, 48.515
maxx, maxy = minx+0.05, miny+0.02
fig.set_xlim(minx, maxx)
fig.set_ylim(miny, maxy)

plt.tick_params(axis='both', labelsize=6) # make the tick label font smaller
fig.ticklabel_format(useOffset=False) # remove the scientific notation fromt he tick labels

# plt.title("Title")
# plt.grid(True)

# plt.show()

plt.savefig("plot.svg", format="svg")

fig.set_axis_off()
plt.savefig("plot_no_axes.svg", format="svg")
