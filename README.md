## Caspian Sea Area Visualization using Satellite Imagery via Google Earth Engine

The main goal of this project is to visualize the changes in the Caspian Sea's area and water level from 1992 to 2023 using satellite shots available in Google Earth Engine. We aim to extract good quality images of the Caspian Sea during this period and apply light Photoshop techniques to reduce clouds and ensure color consistency across different satellites.

### Satellites used:
- 1992-1999: USGS Landsat 5 Level 2, Collection 2, Tier 1
- 2000-2023: MCD43A4.061 MODIS Nadir BRDF-Adjusted Reflectance Daily 500m

### Data Collection and Processing:
To obtain the images, we used 'main.py' with the Earth Engine API and geemap in Google Colab. Running the code in this environment is recommended as the API is already installed by default, and it provides better integration with the map viewer.

After obtaining the images, we utilized the Healing Brush tool and color matching in Adobe Photoshop to enhance consistency between pictures taken over the years. While the brush sacrifices some land details, the scope of this project focuses on the water area, which has remianed largely untouched after the edits. Additionally, we employed DaVinci Resolve to create smooth transitions between the images, color match and brighten them, add year and area data, and finalize the video editing.

### Data Sources:
- Water level data for the Caspian Sea is graciously provided by the Deutsches Geodätisches Forschungsinstitut Technische Universität München, specifically the DAHITI study 'Schwatke, C., Dettmering, D., Bosch, W., and Seitz, F.: DAHITI - an innovative approach for estimating water level time series over inland waters using multi-mission satellite altimetry: , Hydrol. Earth Syst. Sci., 19, 4345-4364, doi:10.5194/hess-19-4345-2015, 2015': [https://dahiti.dgfi.tum.de/en/39/water-level-altimetry/]

### Scripts Overview:
- main.py contains everything for obtaining the initial images from the Google Earth Engine
- caspian_graph.py contains the matplotlib code to build a line graph based on the DAHITI data

### Data Overview:
- 'caspian.csv': CSV file containing water area data based on UNESCO records
- '[caspian_mosaics_raw]([https://drive.google.com/drive/folders/1ahn_LBG-EQzTmfE11JIhwBTP4Y917j8s?usp=drive_link](https://drive.google.com/drive/folders/1m99LPTxmPq9A5Q2w2cSceA6toEuc02qn?usp=sharing))': Folder with initial images collected via 'main.py'
- '[caspian_mosaics_edited]([https://drive.google.com/drive/folders/1phCYtP0CS9inrxAEgmZBY3Jw4Zf6jCST?usp=drive_link](https://drive.google.com/drive/folders/1eXmhIO5ECvuuFB3Rs1mJhd9iFIt-axoC?usp=sharing))': Folder with images after post-processing in Photoshop

### Comparison between raw and edited images based on previous project with the exact same methodology:

![Screenshot 2023-08-04 at 10 58 32](https://github.com/open-data-kazakhstan/-sea-area-visualization/assets/109875855/821115c2-4fc1-43fb-ad3e-98b1852d54ea)

### Resulting line graph:

![Screenshot 2023-08-18 163547](https://github.com/open-data-kazakhstan/caspian-sea-area-visualization/assets/109875855/c61b71a3-922d-419e-b98d-bfa018565df2)

### License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/

Please feel free to contribute to this research project and help us in visualizing the changes in the Caspian Sea over time. Your input is valuable to us!
