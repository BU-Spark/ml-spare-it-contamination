# Spare-it Segmentation Model Deployment

For our deployment phase, we developed a refined version of the copy-paste augmentation which improves the class imbalance and integrates objects from the TACO dataset. We then retrained YOLOv8 with this improved copy-paste augmentation and deployed our best segmentation model to Hugging Face. We also create a pipeline for finetuning with Stable Diffusion to generate synthetic objects which can potentially be integrated into the copy-paste augmentation to diversify the dataset further. 

## File directory

- **`Hugging Face Demo`**: This directory contains the source code for our demo along with instructions on how to run the demo locally. The demo is also hosted on Hugging Face and the link can be found [here](https://huggingface.co/spaces/hengc/Spare-it_fall24).
- **`AI Image Generation`**: This directory contains the pipeline for finetuning Stable Diffusion to generate synthetic objects for different classes in the Spare-it dataset.
- **`deploy_best.pt`**: This file can be used to download our best performing YOLO model from the deployment phase. 
- **`Copy Paste Generator.ipynb`**: This notebook contains the code used to generate the improved version of the copy paste dataset.

## Extra Setup

Notebooks are run with the Spare-it dataset on SCC, so the file paths are specific to the SCC file system. To use the notebooks, ensure that you set the appropriate paths to the dataset containing all your images and labels data. There are more instructions in the notebooks. You will also need to set up your python environment from the `requirements.txt` file. Note that there are different `requirements.txt` files for each folder.

```
pip install -r requirements.txt
```

## Overall Results

Here is the new class distribution after applying our improved copy-paste augmentation. For comparison, see the original class distribution in `3.EDA/images_and_labels.ipynb`.

![output (2)](https://github.com/user-attachments/assets/41868382-15b7-454c-b335-8d58c9948b35)

We then retrained YOLOv8 with Original Spare-it Dataset + Improved Copy-Paste Dataset: 

![results (1)](https://github.com/user-attachments/assets/dad7a1fd-ad60-499a-bd2c-021310c85324)

Here is a detailed comparison of the model's performance by class compared to the baseline model performance: 

<img width="1309" alt="Screenshot 2024-12-08 at 1 30 01 PM" src="https://github.com/user-attachments/assets/194153b1-ebe8-4d29-a549-a6beb8104750">

![Figure_1](https://github.com/user-attachments/assets/04d0d11a-93a9-4032-9cac-f8d54098ca54)

It should be noted that while this model achieves 0.587 mAP@50, we are careful not to directly compare it to the models trained during the POC phase because for the Deployment phase we used an improved version of the validation dataset for a more robust model evaluation which was not used in the POC phase - the details of this are outlined in `4.POC/spare-it-segmentation-model.ipynb`. Therefore, we re-established the baseline performance by retraining the model with just the original Spare-it dataset using the new train-val split and this achieved 0.539 mAP@50.



