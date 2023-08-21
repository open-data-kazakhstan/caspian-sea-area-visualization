# This code is meant to be run in Google Colab for the best experience

import ee
import geemap

# Authenticate and initialize the Earth Engine
# Auth only need to be done once per session, you can comment it afterward
ee.Authenticate()
ee.Initialize()

# Define the bounding box coordinates for the region of interest
region = ee.Geometry.Polygon(
    [[[57.783926555850776, 46.82759854628999],
      [57.783926555850776, 44.0217571843187],
      [61.771963665225776, 44.0217571843187],
      [61.771963665225776, 46.82759854628999]]], None, False)


# Function to get image IDs from the image collection
def get_image_ids(collection):
    image_ids = collection.aggregate_array('system:index')
    return image_ids


# Function to generate mosaic image for a given year
def generate_mosaic(year):
    # Select the Landsat version that suits the time period
    landsat_col = 'MODIS/061/MCD43A4'
    landsat_collection = ee.ImageCollection(landsat_col) \
        .filterBounds(region) \
        .filterDate(str(year) + '-02-01', str(year) + '-10-30') \
        .filter("CLOUD_COVER < 30")  # Best pictures are <5 but not always available

    # Call the function to get the Landsat image IDs
    landsat_image_ids = get_image_ids(landsat_collection)

    # Mosaic the images within the region
    mosaic_image = landsat_collection.mosaic()

    # Print the list of Landsat image IDs to the console
    print('Landsat version:', landsat_col)
    print('Landsat Image IDs for year', year, ':', landsat_image_ids.getInfo())

    # Display the mosaic image on the map
    # Be sure to look up bands and min/max/gamma for each individual Landsat collection
    # For example: https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2
    vis_params = {'bands': 
                  ['Nadir_Reflectance_Band1', 'Nadir_Reflectance_Band4',
                  'Nadir_Reflectance_Band3'],
                  'min': 0.0,
                  'max': 10000.0,
                  'gamma': 1.4}

    # Fit the mosaic inside your selected region
    clipped = mosaic_image.clip(region)
    Map.addLayer(clipped, vis_params, 'Image - ' + str(year))

    # Save the mosaic image as a file.
    # Comment this block when choosing suitable pictures on the map for faster load times
    filename = "mosaic_" + str(year) + ".png"
    geemap.get_image_thumbnail(clipped, filename, vis_params, dimensions=2000)
    geemap.show_image(filename)


# Create the map
Map = geemap.Map()
Map.centerObject(region, 8)

# Iterate over the years and generate mosaic for each year
# This is mainly trial and error due to varying quality and availability of images in collections
# Adjust months, years, cloud cover and vis_params until the images are suitable
for year in range(2001, 2006):
    generate_mosaic(year)

Map.addLayerControl()  # Add layer control to the map
print(Map)
