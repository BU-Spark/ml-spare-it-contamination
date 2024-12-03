# Spare-it Segmentation Model Deployment

For our deployment phase, we developed a refined version of the copy-paste augmentation which improves the class imbalance and integrates objects from TACO and then retrained YOLOv8 with the new copy-paste data. We have also deployed our best segmentation model to Hugging Face.

## File directory

- **`HuggingFace Demo`**: This directory contains the source code for our demo hosted on Hugging Face alsong with instructions on how to run the demo locally. 
- **`deploy_best.pt`**: This file can be used to download our best performing YOLO model from the deployment phase. 
- **`Copy Paste Generator.ipynb`**: This notebook contains the code used to generate the improved version of the copy paste dataset.

## Extra Setup

Several notebooks are run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebooks, ensure that you set the appropriate paths to the dataset containing all your images and labels data. There are more instructions in the notebooks. You will also need to set up your python environment from the `requirements.txt` file. Note that there are different `requirements.txt` files for each folder.

```
pip install -r requirements.txt
```

## Overall Results

Here is the new class distribution with our improved copy-paste dataset:

![output (2)](https://github.com/user-attachments/assets/41868382-15b7-454c-b335-8d58c9948b35)

We then retrained YOLOv8 with Original Spare-it Dataset + Improved Copy-Paste Dataset: 

![results (1)](https://github.com/user-attachments/assets/dad7a1fd-ad60-499a-bd2c-021310c85324)

<img width="356" alt="Screenshot 2024-12-03 at 9 16 26 AM" src="https://github.com/user-attachments/assets/1cf23ceb-6c1e-4dca-99f6-cbb98b39ae65">

This model achieves 0.598 mAP@50, although we are careful not to directly compare it to the models trained during the POC phase because we also used an improved version of the validation dataset which is outlined in `4.POC/spare-it-segmentation-model.ipynb`.



