import folium
from folium import plugins
import rasterio
from matplotlib import cm
import geopandas as gpd
import branca
import numpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from rasterio.plot import reshape_as_image
from PIL import Image
import io

import os
os.environ["SHAPE_RESTORE_SHX"] = "YES"


# Generar mapa para la práctica 4 (archivo .shp)
def generar_mapa_shp(shp_file, output_html):
    gdf = gpd.read_file(shp_file)
    geojson_file = shp_file.replace(".shp", ".geojson")
    gdf.to_file(geojson_file, driver="GeoJSON")
    
    mapa = folium.Map(location=[39, -0.25], tiles='OpenStreetMap', zoom_start=12)
    folium.GeoJson(geojson_file).add_to(mapa)
    folium.LayerControl().add_to(mapa)
    mapa.save(output_html)

# Generar mapa para los archivos raster (.tif)
def generar_mapa_raster(tif_file, output_html, colormap):
    # Leer el archivo raster
    with rasterio.open(tif_file) as src:
        array = src.read(1)  # Leer la primera banda
        bounds = src.bounds  # Extensión geográfica del raster

    # Normalizar los valores para que estén entre 0 y 1
    norm = Normalize(vmin=np.nanmin(array), vmax=np.nanmax(array))
    array_norm = norm(array)

    # Aplicar colormap
    colormap_array = colormap(array_norm)

    # Convertir a imagen (8 bits por canal) y guardar como PNG
    colormap_array = (colormap_array[:, :, :3] * 255).astype(np.uint8)
    image = Image.fromarray(colormap_array)
    png_path = tif_file.replace(".tif", "_overlay.png")  # Guardar PNG junto al archivo original
    image.save(png_path)

    # Crear el mapa con Folium
    mapa = folium.Map(location=[(bounds.top + bounds.bottom) / 2, (bounds.left + bounds.right) / 2], zoom_start=12)

    # Agregar el raster como ImageOverlay
    folium.raster_layers.ImageOverlay(
        image=png_path,  # Ruta al PNG
        bounds=[[bounds.bottom, bounds.left], [bounds.top, bounds.right]],
        opacity=0.7,
        interactive=True,
        name="Mapa Raster"
    ).add_to(mapa)

    # Agregar control de capas
    folium.LayerControl().add_to(mapa)

    # Guardar el mapa como HTML
    mapa.save(output_html)

# Generar mapa para práctica 4
generar_mapa_shp("Practicas/P4/ZONAS_VALIDAS.shp", "Practicas/P4/ZONAS_VALIDAS.html")

# Generar mapas para prácticas 9 y 10
generar_mapa_raster("Practicas/P9/Marti_NBR_post.tif", "Practicas/P9/Marti_NBR_post.html", cm.RdYlGn)
generar_mapa_raster("Practicas/P10/Marti_MNDWI_post.tif", "Practicas/P10/Marti_MNDWI_post.html", cm.Blues)
generar_mapa_raster("Practicas/P10/Marti_MNDWI_post (1).tif", "Practicas/P10/Marti_MNDWI_post (1).html", cm.Greens)
