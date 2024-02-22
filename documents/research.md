# Spare-it Research Document

## *Members: Mustafa Taibah, Jason Oh, Tessa Wu*

## Problem Understanding

Spare-it focuses on leveraging technology to optimize waste management practices, aiming for a more sustainable and efficient approach to recycling. The project is centered around the development of an object detection model with the following objectives:

1. **Object Detection:** The model is tasked with identifying and distinguishing various items placed in the recycling bin. This crucial step involves detecting different types of waste, such as plastics, metals, paper, and more, with high accuracy.

2. **Classification:** After detection, the model will classify objects based on their appropriate disposal categories. This includes determining whether an item belongs in the recycling bin, compost bin, or trash bin. Importantly, the model needs to identify incorrect disposals, pinpointing what type of non-recyclable or wrongly placed items are present in each bin. This capability is essential for enhancing sorting accuracy and facilitating targeted educational efforts on proper recycling practices.

3. **Contamination Rate Estimation:** A separate but related objective is to assess the contamination rate within the recycling bin. This involves calculating the proportion of non-recyclable material present, which is crucial for evaluating the purity of recyclables and the efficiency of recycling efforts. By accurately estimating contamination rates, Spare-it aims to identify areas for improvement in waste management protocols and reduce the environmental impact of improper recycling.

## Research Papers

### 1. Fruit Ripeness Identification Using YOLOv8 Model

- **Summary:** This paper presents a study on the application of deep learning models, particularly YOLOv8 and CenterNet, for the classification of fruits as ripe or overripe based on digital images. It delves into the extraction of visual features and analysis of fruit peel characteristics to accurately predict fruit ripeness. Utilizing custom datasets for training, YOLOv8 demonstrated a remarkable classification accuracy of 99.5%, attributed to its CSP and C2f modules. This underscores YOLOv8's superior performance in identifying fruit ripeness compared to CenterNet.
- **Link:** [Springer](https://link.springer.com/article/10.1007/s11042-023-16570-9)

### 2. Advancing Plastic Waste Classification and Recycling Efficiency: Integrating Image Sensors and Deep Learning Algorithms

- **Summary:** This article explores an innovative method to enhance plastic waste classification and recycling efficiency by integrating image sensors with the YOLO deep learning model. Focusing on the physical shape of waste, this approach addresses the challenge of distinguishing chemically similar plastics like PET and PET-G. With an accuracy exceeding 91.7%, this method outperforms traditional sorting techniques, promising a more effective, scalable, and adaptable system for various applications. This significantly advances recycling processes and contributes to environmental sustainability.
- **Link:** [MDPI](https://www.mdpi.com/2076-3417/13/18/10224)

## Open Source

### YOLOv8

- **Usage:** YOLOv8 can be applied in a variety of scenarios that require real-time object detection.
- **Links:** 
  - [Ultralytics GitHub](https://github.com/ultralytics/ultralytics)
  - [YOLO-MS GitHub](https://github.com/FishAndWasabi/YOLO-MS)
- **About YOLO-MS:** YOLO-MS emphasizes multi-scale representation learning for real-time object detection, aiming to enhance the model's ability to identify smaller or irregularly shaped waste components.
