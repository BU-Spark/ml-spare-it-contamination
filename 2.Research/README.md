# Spare-it Research Document Fall 2024

## *Members: Tia Hannah, Devon Solheim, Heng Chang, Arjun Chandra*

## Problem Understanding

Spare-it focuses on leveraging technology to optimize waste management practices, aiming for a more sustainable and efficient approach to recycling. This project is centered around the improvement of last semester's object detection model with the following objectives:

1. **Object Detection:** The model is tasked with identifying and distinguishing various items placed in the recycling bin. This crucial step involves detecting different types of waste, such as plastics, metals, paper, and more, with high accuracy.

2. **Classification:** The model will also classify objects based on their appropriate disposal categories. This includes determining whether an item belongs in the recycling bin, compost bin, or trash bin. Importantly, the model needs to identify incorrect disposals, pinpointing what type of non-recyclable or wrongly placed items are present in each bin. This capability is essential for enhancing sorting accuracy and facilitating targeted educational efforts on proper recycling practices.

3. **Contamination Rate Estimation:** A separate but related objective is to assess the contamination rate within the recycling bin. This involves calculating the proportion of non-recyclable material present, which is crucial for evaluating the purity of recyclables and the efficacy of recycling efforts. By accurately estimating contamination rates, Spare-it aims to identify areas for improvement in waste management protocols and reduce the environmental impact of improper recycling.


## Literature Review



### 1. A Survey on Image Data Augmentation for Deep Learning

- **Summary:** This survey paper discusses a variety of image data augmentation techniques for training deep convolutional networks, from simple geometric transformations to feature space augmentations to neural style transfer. All of these augmentations are described in detail with reference to other works that demonstrate their effectiveness on benchmark datasets. The authors also mention several augmentations which do not appear useful to the human observer (e.g. SamplePairing) but improve model performance, and this is a useful insight to keep in mind when considering data augmentation. 
- **Link:** [Journal of Big Data](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-019-0197-0)

### 2. A Survey on Addressing High-Class Imbalance in Big Data

- **Summary:** This survey paper reviews the approaches used to address class imbalance in both traditional and big data. For traditional data, the approaches are divided into Data-Level methods and Algorithm-Level methods. Examples of Data-Level methods include over-sampling, under-sampling, and feature selection. Algorithm-Level methods include ensemble techniques and class level objective function weights. These approaches are similar for big data, although further considerations are mentioned such as the MapReduce framework which may not be as relevant for our use case. 
- **Link:** [Journal of Big Data](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-018-0151-6)

### 3. An MRS-YOLO Model for High-Precision Waste Detection and Classification

- **Summary:** This paper presents MRS-YOLO, a YOLO model designed specifically to address the challenge of detecting and classifying urban garbage effectively. The model is equipped with three novel components: (1) An enhanced C2f feature extraction method (YOLOv8) using a multidimenional convolution approach (2) Integrated RepViT module and (3) An enhanced objective function using SlideLoss_IOU. Each of these components are validated with ablation studies in addition to the overall enhanced model which achieves 0.745 mAP. The dataset used contains ~12,000 images of trash across 10 categories, and there is relatively little class imbalance. 
- **Link:** [MDPI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11244501/)


### 4. Advancing Plastic Waste Classification and Recycling Efficiency: Integrating Image Sensors and Deep Learning Algorithms

- **Summary:** This article explores an innovative method to enhance plastic waste classification and recycling efficiency by integrating image sensors with the YOLO deep learning model. Focusing on the physical shape of waste, this approach addresses the challenge of distinguishing chemically similar plastics like PET and PET-G. The dataset contains 2,000 annotated samples, and is augmented to ~50,000 samples using rotation, zoom, and other techniques.  With an accuracy exceeding 91.7%, this method outperforms traditional sorting techniques, promising a more effective, scalable, and adaptable system for various applications. This significantly advances recycling processes and contributes to environmental sustainability.
- **Link:** [MDPI](https://www.mdpi.com/2076-3417/13/18/10224)

### 5. Waste Detection System Based on Data Augmentation and YOLO_EC

- **Summary:** This study focuses on improving waste detection using a modified version of the YOLO model, YOLO_EC, which is enhanced through generative data augmentation techniques, specifically DCGAN with an improved objective function. This approach aims to address the challenges of detecting various types of waste, especially in complex environments with obscured or small objects. The study demonstrates the effectiveness of YOLO_EC in accurately identifying and classifying waste materials on a dataset of ~1700 images with 4 categories: (1) recyclable waste (2) other waste (3) harmful waste (4) kitchen waste. The work done last semester was very similar to this approach, where YOLOv8 was used for object detection and the dataset was augmented using DCGAN with the standard BCE objective. 
- **Link:** [MDPI](https://www.mdpi.com/1424-8220/23/7/3646)








## Open Source


### Libraries

#### YOLOv8

- **Usage:** YOLOv8 can be applied in a variety of scenarios that require real-time object detection.
- **Links:** 
  - [Ultralytics GitHub](https://github.com/ultralytics/ultralytics)

#### HuggingFace Diffusers 

- **Usage:** The HuggingFace Diffusers library provides support for building end-to-end diffusion systems, and also contains starter code for fine-tuning Stable Diffusion.
- **Links:** 
  - [GitHub Link](https://github.com/huggingface/diffusers/tree/main)


### Datasets 

#### Waste Datasets
- **About:** This is a GitHub repository which lists datasets that contain any kind of litter, garbage, waste, or trash. It also contains relevation information about each dataset, including the number of classes, subsclasses, images, and annotation type. There are also representative images from each dataset in the Description section. 
- **Link:** [Waste Datasets](https://github.com/AgaMiko/waste-datasets-review?tab=readme-ov-file)

#### TACO (Trash Annotations in Context)

- **About:** TACO is an open waste image dataset aimed at improving litter detection and classification. It consists of thousands of images annotated for research in waste management, providing a valuable resource for training AI models in recognizing various types of litter. The dataset is continuously growing, with contributions from the community, showcasing the power of collaborative efforts in tackling environmental challenges.
- **Link:** [TACO](http://tacodataset.org/)


### Projects

#### Litter Detection with Yolov8
- **About:** This GitHub repository implements YOLOv8 to detect trash/litter in the Trash Annotations in Context (TACO) dataset.
- **Link:** [GitHub](https://github.com/jeremy-rico/litter-detection)

#### Waste Classification using CNN
- **About:** This repository showcases a project dedicated to waste classification using convolutional neural networks (CNNs). It focuses on developing a machine learning model capable of distinguishing different waste types, such as plastic, paper, metal, and glass, to improve recycling processes.
- **Link:** [GitHub](https://github.com/aniass/Waste-Classification)
