import arcpy
import rasterio

# Ruta de la imagen raster de entrada (16 bits)
input_raster = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/20220808_145647_90_2481_3B_AnalyticMS_SR_8b_clip.tif"

# Ruta de la imagen raster de salida (8 bits)
output_raster = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bitsArcPy.tif"

# Definir el rango de valores para la conversión
input_min16 = 0  # Valor mínimo en la imagen de 16 bits
input_max16 = 8883  # Valor máximo en la imagen de 16 bits

output_min8 = 0  # Valor mínimo para la imagen de 8 bits
output_max8 = 255  # Valor máximo para la imagen de 8 bits
# Ruta de salida para las bandas individuales
output_red_band = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bits_image/banda_roja.tif"
output_green_band = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bits_image/banda_verde.tif"
output_blue_band = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bits_image/banda_azul.tif"

# Extraer la banda roja (banda 1)

# arcpy.RasterToOtherFormat_conversion(
#     input_raster, output_red_band, "TIFF", "", "", "", "", "", "", "TIFF", "BAND 4"
# )
# arcpy.RasterToOtherFormat_conversion(
#     input_raster,
#     output_green_band,
#     "TIFF",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "TIFF",
#     "BAND " + "3",
# )
# arcpy.RasterToOtherFormat_conversion(
#     input_raster,
#     output_blue_band,
#     "TIFF",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "",
#     "TIFF",
#     "BAND " + "2",
# )

arcpy.management.CopyRaster(
    input_raster,
    output_blue_band,
    "",
    "",
    "",
    "",
    "",
    "",
    "8_BIT_UNSIGNED",
    "",
    "",
    "",
    "",
    "USE_PIXEL_VALUES",
    2,
)


output_composite = "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bits_image/composicion_rgb.tif"

# Componer las tres bandas en una imagen RGB
arcpy.CompositeBands_management(
    [output_red_band, output_green_band, output_blue_band], output_composite
)


# print("Conversión completada.")
pixel_type = "8_BIT_UNSIGNED"

# Realizar la conversión utilizando CopyRaster
# arcpy.management.CopyRaster(input_raster, pixel_type)
arcpy.management.CopyRaster(
    output_composite,
    "C:/Users/ACER/Downloads/Caqueza__psscene_analytic_8b_sr_udm2/PSScene/8bits0301_rgb_ArcPy.tif",
    "",
    "",
    "",
    "",
    "",
    "8_BIT_UNSIGNED",
)
print("Conversión completada.")
