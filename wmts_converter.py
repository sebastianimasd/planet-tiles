import requests
import io
from PIL import Image
from owslib.wmts import WebMapTileService
import math
from rasterio.io import MemoryFile
from rasterio.enums import Resampling


def calculate_tile_row_col(lat, lon, zoom):
    # Convierte latitud y longitud a coordenadas EPSG:3857
    x = lon * 20037508.34 / 180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * 20037508.34 / 180

    # Calcula las coordenadas de teselas
    n = 2.0**zoom
    tile_col = int((x + 20037508.34) / (2 * 20037508.34 / n))
    tile_row = int((20037508.34 - y) / (2 * 20037508.34 / n))

    return tile_row, tile_col


# Coordenadas de ejemplo (latitud, longitud) y nivel de zoom
lat = 4.68
lon = -74.11
zoom = 15  # Nivel de zoom

tile_row, tile_col = calculate_tile_row_col(lat, lon, zoom)

print(f"TILEROW: {tile_row}, TILECOL: {tile_col}")


# URL del servicio WMTS y parámetros
wmts_url = "https://api.planet.com/basemaps/v1/mosaics/wmts?api_key=PLAK630572b322ac487891546154cb3fe604"
layer = "global_monthly_2016_01_mosaic"
style = "default"
tile_matrix_set = "urn:ogc:def:crs:OGC:2:84"
TileMatrix = zoom
TileRow = tile_row
TileCol = tile_col


tile_custom = "https://tiles.planet.com/basemaps/v1/planet-tiles/global_monthly_2016_07_mosaic/gmap/{}/{}/{}.png?api_key=PLAK630572b322ac487891546154cb3fe604".format(
    TileMatrix, TileCol, TileRow
)
print(tile_custom)
response = requests.get(tile_custom)
print(response)

wmts = WebMapTileService(wmts_url)
capa = list(wmts.contents)[0]
info_capa = wmts.contents[capa]
# Obtener información sobre la cuadrícula de teselas

tile_data = io.BytesIO(response.content)
image = Image.open(tile_data)

image.save("imagen.tif")
image.show()


# Lee la respuesta como un archivo raster
with MemoryFile(tile_data) as memfile:
    with memfile.open() as dataset:
        # Aquí puedes realizar algún procesamiento o re-muestreo si es necesario
        # Por ejemplo, puedes cambiar el tamaño de la imagen utilizando Resampling.bilinear

        # Guarda el resultado en un archivo TIFF
        output_file = "salida.tif"
        with rasterio.open(
            output_file,
            "w",
            driver="GTiff",
            width=dataset.width,
            height=dataset.height,
            count=dataset.count,
            dtype=dataset.dtypes[0],
            crs=dataset.crs,
        ) as dst:
            dst.write(dataset.read(1))

print("Conversión completada.")
