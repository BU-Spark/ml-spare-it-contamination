# Spare-it Exploratory Data Analysis (EDA)

We have provided several Jupyter Notebook for our Exploratory Data Analysis. The file directory and any other necessary setup details are explained below. 


## File directory

- **`External dataset integration(TACO)`**: This directory contains code to transform TACO dataset annotations to the format which Spare-it uses and includes sample annotations.

- **`images_and_labels.ipynb`**: This file contains an analysis of the images and labels in the dataset, including details about class imbalance and other potential issues. 

- **`Performance vs Sample Counts`**: This directory contains graphs of the previous segmentation model performance vs # of trainig examples by class. 

## Extra Setup

This notebook is run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebook, ensure that you set the appropriate paths to the dataset containing all your images and labels data. You will also need to install the following packages: 

```
pip install cleanvision
```

