# Spare-it Proof-of-Concept (POC)

We have provided several Jupyter Notebooks for our POC. The file directory and any other necessary setup details are explained below. 

## File directory

- **`best.pt`**: This file can be used to download our best YOLO model. 
- **`spare-it-segmentation-model.ipynb`**: This notebook contains the code to convert the Spare-it dataset, augmented datasets, and external datasets to YOLOv8 format, train the YOLOv8 model, and analyze the results. 
- **`Copy Paste Generator.ipynb`**: This notebook contains the code used to generate the copy paste dataset.

## Extra Setup

Several notebooks are run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebooks, ensure that you set the appropriate paths to the dataset containing all your images and labels data. There are more instructions in the notebooks. You will also need to set up your python environment from the `requirements.txt` file. Note that the `Image Generation` directory has a separate `requirements.txt` file.

```
pip install -r requirements.txt
```

## Overall Results
![results (1)](https://github.com/user-attachments/assets/e44aba02-55c2-4571-8969-0b2c13317a34)
