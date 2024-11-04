# Spare-it Proof-of-Concept (POC)

We have provided several Jupyter Notebooks for our POC. The file directory and any other necessary setup details are explained below. 

## File directory

- **`Image Generation`**: This directory contains code to experiment with fine-tuning Stable Diffusion on specific categories from the Spare-it dataset. 
- **`TACO`**: This directory contains code to download and transform the TACO dataset into Spare-it format so that it can be integreated easily into the training pipeline.
- **`best.pt`**: This file can be used to download our best performing YOLO model. 
- **`Copy Paste Generator.ipynb`**: This notebook contains the code used to generate the copy paste dataset.
- **`postprocessing.py`**: This script analyzes the images in the Spare-it dataset and records information that can be used in postprocessing to distinguish between general classes for more fine-grained classification. 
- **`spare-it-segmentation-model.ipynb`**: This notebook contains the code to convert the Spare-it dataset, augmented datasets, and external datasets to YOLOv8 format, train the YOLOv8 model, and analyze the results. 

## Extra Setup

Several notebooks are run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebooks, ensure that you set the appropriate paths to the dataset containing all your images and labels data. There are more instructions in the notebooks. You will also need to set up your python environment from the `requirements.txt` file. Note that there are different `requirements.txt` files for each folder.

```
pip install -r requirements.txt
```

## Overall Results

We trained the YOLOv8 model with several different training configurations:
1. Original Spare-it Dataset with default augmentation 
2. Original Spare-it Dataset with YOLO copy-paste augmentation (flip and mixup)
3. Original Spare-it Dataset + TACO with default augmentation
4. Original Spare-it Dataset + our copy-paste dataset with default augmentation
4. Original Spare-it Dataset + our copy-paste dataset + TACO dataset with default augmentation

We found that method 4. worked the best. Compared to the baseline model (method 1.) which achieves 0.598 mAP@50, our best model achieved 0.685 mAP@50. The results for this model are shown below. 

![results (1)](https://github.com/user-attachments/assets/e44aba02-55c2-4571-8969-0b2c13317a34)
