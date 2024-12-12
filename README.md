# Spare-it: Contamination Identification

## Project Description

[Spare-it](https://www.spare-it.com/) is dedicated to assisting businesses, office owners, and universities in obtaining real-time data on various types of workspace waste, including general waste, recycling, electronics, energy, water, and travel. The organization motivates employees and students to minimize waste through awareness and actionable intelligence. The overarching goal of this project is to develop a machine learning model capable of predicting contamination and identifying missed opportunities for recycling and waste management.

## Directory Explanation

- **`/1.ProjectOutline`**: This directory contains the project outline, where we've detailed the stakeholders' goals for the project and outlined the steps our team needs to take to achieve those goals.

- **`/2.Research`**: This directory contains research related to the project, including recent papers related to data augmentation and waste detection.

- **`/3.EDA`**: This directory contains our exploratory data analysis on the labels and images provided by Spare-it as well as the performance of the previously developed segmentation model.

- **`/4.POC`**: This directory contains our proof-of-concept, where we've trained the YOLOv8 model on the Spare-it dataset with external datasets (TACO) and different augmentations. It also contains experimental work to use Stable Diffusion for generating synthetic images of categories in the Spare-it dataset and a script for postprocessing in case we decide to merge classes. 

- **`/5.Deployment`**: This directory contains an improved version of the copy-paste augmentation aimed at balancing the class distribution and integrating objects from the TACO dataset. It also contains our best YOLOv8 model from the deployment phase which we deployed to Hugging Face using Streamlit and a configurable pipeline for fine-tuning stable diffusion for synthetic data generation.

- **`/SPRING 2024 ARCHIVE`**: This directory contains the work done on this project in the Spring 2024 semester.

- **`/dataset-documentation`**: This directory contains documentation about the dataset provided by Spare-it.
 
- **`/documents`**: This directory contains our final class presentation as well as our final poster presentation.

## Overview

This project aimed to identify contamination and improve recycling and waste management practices. By leveraging image detection models, data analysis, and real-time monitoring, we've created a system that aligns with Spare-it's mission of minimizing waste through actionable intelligence. Each directory in this project represents a key stage of our process, from outlining the project goals to deploying the final model. The various documents and code files showcase our research, development, and implementation efforts, culminating in a machine learning model that enhances sustainability initiatives.

## Demo

A link to our Hugging Face Demo can be found here: [DEMO](https://huggingface.co/spaces/hengc/Spare-it_fall24)

## Results 

Using the tools we built, we were able to train a model which achieves 0.587 mAP@50 on the 43 categories that we focused on this semester compared to the baseline model which achieves 0.539 mAP@50. These performance results are summarized below. 

<img width="1309" alt="Screenshot 2024-12-08 at 1 30 01 PM" src="https://github.com/user-attachments/assets/099d67b3-f409-474b-9684-cc7fbef27661">

![Figure_1](https://github.com/user-attachments/assets/e5d15f96-0ab9-4f95-ad8d-6fd23d228f81)

## Reproducibility 

We aimed to make our project easily reproducible. Given this, all of the folders containing any sort of code (usually `.ipynb` or `.py` files) have their own `README.md` files which give detailed instructions for setup. The code itself is also thoroughly commented. In terms of dependencies, we have provided several different `requirements.txt` files throughout the codebase. Each of these usually corresponds to the dependencies needed to run a specific tool we have built (e.g. TACO integration, AI Image Generation) or analysis we have done (e.g. EDA). We hope that this will allow others to only install only the dependencies needed for the tools that they wish to use. Also, as a general note, many of the filepaths used in the codebase are specific to the SCC file system, and these will need to be replaced appropriately when reproducing the results. To help with this, we have tried to provide comments everywhere that SCC specific filepaths are used. 

## Future Work

We have several recommendations for future work in case there is another student team that works on this project. First, we recommend that the team start by leveraging the AI Image Generation tools that we built to integrate synthetic data into the training pipeline. We were not able to achieve this due to time constraints, but it would be a very interesting first step to try and we have provided most of the code that would be needed to set this up. Second, we recommend the team experiment more with hyperparameter optimization as this was not something we explored in detail but it could yield a marginal performance boost. The team should also note that hyperparameters are not just limited to those provided in the Ultarlytics library for YOLOv8 but also include hyperparameters for tools that we built this semester such as how much copy-paste to apply to balance the class distribution. Finally, we recommend that the team begin to explore how to integrate YOLOv8 with a real-time detection system as this is the ultimate goal of the project. More details for future work are provided in the `documents` folder in our final presentation. 
