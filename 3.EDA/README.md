# Spare-it Exploratory Data Analysis (EDA)

We have provided several Jupyter Notebooks for our Exploratory Data Analysis. The file directory and any other necessary setup details are explained below. 


## File directory

- **`External dataset integration(TACO)`**: This directory contains code to transform TACO dataset annotations to the format which Spare-it uses and includes sample annotations.

- **`Performance vs Sample Counts`**: This directory contains graphs of the previous segmentation model performance vs # of training examples by class.

- **`gini.ipynb`**: This notebook contains functions to transform the GINI dataset annotations to the format which Spare-it uses.

- **`Image Stiching.ipynb`**: This notebook contains a demonstration of data augmentation via combining segments of different images within the Spare-it dataset. 

- **`images_and_labels.ipynb`**: This notebook contains an analysis of the images and labels in the dataset, including details about class imbalance and other potential issues. 


## Extra Setup

Several notebooks are run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebooks, ensure that you set the appropriate paths to the dataset containing all your images and labels data. You will also need to install the following packages in your python environment: 

```
pip install cleanvision
pip install pandas
pip install numpy 
pip install matplotlib
pip install torch 
pip install pycocotools
```

