## External Datasets: TACO

### Overview

This directory contains code that can be used to load and transform the TACO annotations into the format that Spare-it uses.

### File directory

- **`Integration_of_External_Datasets_Report.pdf`**: This pdf file contains a report of our analysis of publicly available external datasets and justifies our decision for ultimately integrating TACO. 
- **`TACO image downloader.py`**: This notebook contains the code to download the TACO images from their urls. 
- **`Taco_Dataset_Transformation.ipynb`**: This notebook contains the code used to generate the transformed TACO json annotations. 

### Class Mapping:

We use the following standard to map the labels in the TACO dataset to the labels in the Spare-it dataset:

![image](https://github.com/user-attachments/assets/c9395aaa-f564-472c-86b0-d591c51a729c)
