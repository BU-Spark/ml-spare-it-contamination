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

## Overview

This project aimed to identify contamination and improve recycling and waste management practices. By leveraging image detection models, data analysis, and real-time monitoring, we've created a system that aligns with Spare-it's mission of minimizing waste through actionable intelligence. Each directory in this project represents a key stage of our process, from outlining the project goals to deploying the final model. The various documents and code files showcase our research, development, and implementation efforts, culminating in a machine learning model that enhances sustainability initiatives.

## Demo

A link to our Hugging Face Demo can be found here: [DEMO](https://huggingface.co/spaces/hengc/Spare-it_fall24)

## Results 

To be updated 
