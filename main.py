"""
Make nice ascii images of maps, drawing on inspiration from pretty maps.
We want to make it possible to see you map data in your shell.
"""
import subprocess

from shapely.geometry import box
import geopandas as gpd
import matplotlib.pyplot as plt


def main():
    gdf_poi = gpd.read_file("austin_pois.geojson")
    gdf_us = gpd.read_file("us-states.geojson")
    
    f, ax = plt.subplots()

    gdf_us.boundary.plot(ax=ax, color='black')
    gdf_poi.plot(marker='o', color='black', markersize=5, ax=ax)

    gdf_combo = gdf_us[gdf_us.geometry.apply(lambda x: x.intersects(gdf_poi.geometry).any())]

    x1, y1, x2, y2 = box(*gdf_combo.total_bounds).buffer(0.5).bounds

    ax.set_xlim((x1, x2))
    ax.set_ylim((y1, y2))
    ax.axis('off')

    plt.savefig('test.png')

    subprocess.run("ascii-image-converter test.png --negative -s .", shell=True)


if __name__ == "__main__":
    main()
