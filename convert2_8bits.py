import rasterio
from rasterio import plot
from rasterio.plot import show
import numpy as np
from matplotlib import pyplot
from PIL import Image

input_image_path = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/20220808_145647_90_2481_3B_AnalyticMS_SR_8b_clip.tif"
output_image_path = (
    "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bits.tif"
)

with rasterio.open(input_image_path) as src:
    # Lee los datos de la imagen
    metadata = src.meta
    left, top = src.xy(0, 0)

    # Imprime la información

    print("Coordenadas geoespaciales:")
    print(f"Superior Izquierda: {left}")
    print(f"Superioz izquierda: {top}")

    r = src.read(6)
    g = src.read(4)
    b = src.read(2)
    rgb = [r, g, b]
    rgb_image = np.stack((r, g, b), axis=0)
    print(rgb, " <- rgb | np.stack -> ", rgb_image)
    perfil = {
        "driver": "GTiff",
        "dtype": "uint8",
        "count": 3,
        "width": src.width,
        "height": src.height,
    }
    # show(rgb_image)
    # print(data)

    min_val = np.min(rgb)
    max_val = np.max(rgb)

    print(min_val)
    print(max_val)

    scaled_data = ((rgb - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    scaled_data_2 = ((rgb_image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    metadata = src.meta
    left, bottom, right, top = src.bounds

    # Imprime la información

    print("Coordenadas geoespaciales Imagen de entrada :")
    print(f"Izquierda: {left}")
    print(f"Inferior: {bottom}")
    print(f"Derecha: {right}")
    print(f"Superior: {top}")

    # print(scaled_data)
    # # Actualiza los metadatos para reflejar el cambio a 8 bits

    profile = src.profile
    print(profile)
    profile.update(dtype=rasterio.uint8, count=1)
    print(profile)
    # show(scaled_data, transform=src.transform)
    # show(scaled_data_2, transform=src.transform)

    print("tipo de datos: ", scaled_data.dtype)
    print("Firma del elemento : ", scaled_data.shape)
    print("Dimensiones forma: ", scaled_data.ndim)

    with rasterio.open(output_image_path, "w", **perfil) as dst:
        dst.write(scaled_data_2)
