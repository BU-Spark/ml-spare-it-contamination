# Spare-it Segmentation Model Deployment

For our deployment phase, we developed a refined version of the copy-paste augmentation which improves the class imbalance and integrates objects from TACO. We then retrained YOLOv8 with this improved copy-paste augmentation and deployed our best segmentation model to Hugging Face. We also create a pipeline for finetuning with Stable Diffusion to generate synthetic objects which can potentially be integrated into the copy-paste augmentation to diversify the dataset further. 

## File directory

- **`Hugging Face Demo`**: This directory contains the source code for our demo hosted on Hugging Face alsong with instructions on how to run the demo locally. The demo is also hosted on Hugging Face and the link can be found [here](https://huggingface.co/spaces/hengc/Spare-it_fall24).
- **`AI Image Generation`**: This directory contains the pipeline for finetuning Stable Diffusion to generate synthetic objects for different classes in the Spare-it dataset.
- **`deploy_best.pt`**: This file can be used to download our best performing YOLO model from the deployment phase. 
- **`Copy Paste Generator.ipynb`**: This notebook contains the code used to generate the improved version of the copy paste dataset.

## Extra Setup

Notebooks are run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebooks, ensure that you set the appropriate paths to the dataset containing all your images and labels data. There are more instructions in the notebooks. You will also need to set up your python environment from the `requirements.txt` file. Note that there are different `requirements.txt` files for each folder.

```
pip install -r requirements.txt
```

## Overall Results

Here is the new class distribution after applying our improved copy-paste augmentation:

![output (2)](https://github.com/user-attachments/assets/41868382-15b7-454c-b335-8d58c9948b35)

We then retrained YOLOv8 with Original Spare-it Dataset + Improved Copy-Paste Dataset: 

![results (1)](https://github.com/user-attachments/assets/dad7a1fd-ad60-499a-bd2c-021310c85324)

<img width="356" alt="Screenshot 2024-12-03 at 9 16 26 AM" src="https://github.com/user-attachments/assets/1cf23ceb-6c1e-4dca-99f6-cbb98b39ae65">

This model achieves 0.587 mAP@50, although we are careful not to directly compare it to the models trained during the POC phase because we also used an improved version of the validation dataset for a more robust model evaluation which was not used in the POC phase. The details of this are outlined in `4.POC/spare-it-segmentation-model.ipynb`. Therefore, we also trained the model with just the original Spare-it dataset using the new train-val split and this yielded a baseline performance of 0.539 mAP@50.



