# Spare-it Research Document

## *Members: Mustafa Taibah, Jason Oh, Tessa Wu*

## Problem Understanding

Spare-it focuses on leveraging technology to optimize waste management practices, aiming for a more sustainable and efficient approach to recycling. The project is centered around the development of an object detection model with the following objectives:

1. **Object Detection:** The model is tasked with identifying and distinguishing various items placed in the recycling bin. This crucial step involves detecting different types of waste, such as plastics, metals, paper, and more, with high accuracy.

2. **Classification:** After detection, the model will classify objects based on their appropriate disposal categories. This includes determining whether an item belongs in the recycling bin, compost bin, or trash bin. Importantly, the model needs to identify incorrect disposals, pinpointing what type of non-recyclable or wrongly placed items are present in each bin. This capability is essential for enhancing sorting accuracy and facilitating targeted educational efforts on proper recycling practices.

3. **Contamination Rate Estimation:** A separate but related objective is to assess the contamination rate within the recycling bin. This involves calculating the proportion of non-recyclable material present, which is crucial for evaluating the purity of recyclables and the efficiency of recycling efforts. By accurately estimating contamination rates, Spare-it aims to identify areas for improvement in waste management protocols and reduce the environmental impact of improper recycling.

## Research Papers

### 1. Advancing Plastic Waste Classification and Recycling Efficiency: Integrating Image Sensors and Deep Learning Algorithms

- **Summary:** This article explores an innovative method to enhance plastic waste classification and recycling efficiency by integrating image sensors with the YOLO deep learning model. Focusing on the physical shape of waste, this approach addresses the challenge of distinguishing chemically similar plastics like PET and PET-G. With an accuracy exceeding 91.7%, this method outperforms traditional sorting techniques, promising a more effective, scalable, and adaptable system for various applications. This significantly advances recycling processes and contributes to environmental sustainability.
- **Link:** [MDPI](https://www.mdpi.com/2076-3417/13/18/10224)

### 2. Waste Detection System Based on Data Augmentation and YOLO_EC

- **Summary:** The study focuses on improving waste detection using a novel approach. The authors propose a modified version of the YOLO model, which is enhanced through advanced data augmentation techniques. This approach aims to address the challenges of detecting various types of waste, especially in complex environments with obscured or small objects. The study demonstrates the effectiveness of YOLO_EC in accurately identifying and classifying waste materials. The results indicate that the model, with its improved data processing and learning capabilities, offers a significant advancement over traditional methods, potentially leading to more efficient and effective waste management solutions.
- **Link:** [MDPI](https://www.mdpi.com/1424-8220/23/7/3646)

### 3. **AI-Driven Solutions for Enhanced Waste Management and Recycling in Urban Areas**

- **Summary:** Addressing the pressing challenges of waste management in dense urban landscapes, this study showcases the pivotal role of artificial intelligence (AI) in revolutionizing waste handling. AI's smart solutions—from dynamic waste collection optimization to precision-driven sorting—underline a significant leap towards sustainability. By integrating AI, cities can not only navigate the complexities of high-volume waste management but also ensure the efficacy and environmental integrity of recycling processes. This narrative reinforces the value of adopting AI in waste detection models, emphasizing a promising pathway to enhance urban sustainability and operational efficiency, thereby directly aligning with our project's ambition to foster a cleaner, greener future.
- **Link:** [Vectoral Journal](https://vectoral.org/index.php/IJSICS/article/view/9)

### 4. Waste Classification for Sustainable Development Using Image Recognition with Deep Learning Neural Network Models

- **Summary:** The study focuses on the use of deep learning, specifically the EfficientNet-B0 model, to classify different types of waste. This model, known for its accuracy and efficiency, is adapted to better suit specific local waste characteristics, enhancing its performance in different regions. Such customization makes the model nearly as accurate as its more complex counterparts, like EfficientNet-B3, but with greater efficiency and less computational demand. This model offers a foundation in selecting and tuning a model that is not only effective in accurate classification but also efficient in processing, adaptable to regional variations, and capable of future enhancements for more detailed waste categorization and integration into broader smart city initiatives.
- **Link:** [MDPI](https://www.mdpi.com/2071-1050/14/12/7222)

### 5. **Data-driven Technologies and Artificial Intelligence in Circular Economy and Waste Management Systems: A Review**

- **Summary:** This review paper delves into the applications of data-driven technologies and artificial intelligence (AI) in the realm of waste management and the transition towards a circular economy. It surveys current applications, identifying gaps such as the limited availability of open waste data, and proposes areas for future research and development. Highlighting AI applications in robotic waste sorting and the importance of open data sets like RecycleNet, TrashNet, and TACO, the paper underscores the potential of collaborative, data-driven initiatives to advance sustainable waste management practices. The review points to the need for open data and AI to foster innovation in recycling and waste management systems.
- **Link:** [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/9629183)

### 6. Fruit Ripeness Identification Using YOLOv8 Model

- **Summary:** This paper presents a study on the application of deep learning models, particularly YOLOv8 and CenterNet, for the classification of fruits as ripe or overripe based on digital images. It delves into the extraction of visual features and analysis of fruit peel characteristics to accurately predict fruit ripeness. Utilizing custom datasets for training, YOLOv8 demonstrated a remarkable classification accuracy of 99.5%, attributed to its CSP and C2f modules. This underscores YOLOv8's superior performance in identifying fruit ripeness compared to CenterNet.
- **Link:** [Springer](https://link.springer.com/article/10.1007/s11042-023-16570-9)

### 7. Deep Learning for Digital Image Processing in Plant Recognition

- **Summary:** This study explores the effectiveness of deep learning in image recognition compared to traditional machine learning methods like Support Vector Machines (SVM), focusing on the natural handling of two-dimensional image data by deep learning technologies. It highlights deep learning's superiority in feature extraction and recognition accuracy through a case study on handwritten digit recognition. The findings underscore deep learning's potential for improving automatic image recognition processes, offering insights into its advantages over conventional methods.
- **Link:** [IOP Science](https://iopscience.iop.org/article/10.1088/1742-6596/1314/1/012148/meta)

## Open Source

### YOLOv8

- **Usage:** YOLOv8 can be applied in a variety of scenarios that require real-time object detection.
- **Links:** 
  - [Ultralytics GitHub](https://github.com/ultralytics/ultralytics)
  - [YOLO-MS GitHub](https://github.com/FishAndWasabi/YOLO-MS)
- **About YOLO-MS:** YOLO-MS emphasizes multi-scale representation learning for real-time object detection, aiming to enhance the model's ability to identify smaller or irregularly shaped waste components.

### Deep Learning for Image Recognition

- **About:** This GitHub repository offers a collection of resources and tools for applying deep learning in image recognition tasks. It includes implementations for various deep learning models, making it a valuable asset for researchers and developers working on image recognition, including plant identification, disease detection, and more.
- **Link:** [GitHub - Deep Learning for Image Recognition](https://github.com/SanketD92/Deep-Learning-For-Image-Recognition)

### Waste Classification using ResNet152
- **About:** This GitHub repository presents a project that utilizes ResNet152, a deep convolutional neural network, for the purpose of classifying waste. 
- **Link:** [GitHub](https://github.com/VIJAY-GADRE/Waste_Classification_using_ResNet152)

### Waste Classification using CNN
- **About:** This repository showcases a project dedicated to waste classification using convolutional neural networks (CNNs). It focuses on developing a machine learning model capable of distinguishing different waste types, such as plastic, paper, metal, and glass, to improve recycling processes.
- **Link:** [GitHub](https://github.com/aniass/Waste-Classification)

### TACO (Trash Annotations in Context)

- **About:** TACO is an open waste image dataset aimed at improving litter detection and classification. It consists of thousands of images annotated for research in waste management, providing a valuable resource for training AI models in recognizing various types of litter. The dataset is continuously growing, with contributions from the community, showcasing the power of collaborative efforts in tackling environmental challenges.
- **Link:** [TACO](http://tacodataset.org/)

### Litterati

- **About:** Litterati is a mobile app that engages the community in identifying and cataloging litter through photography. With millions of images labeled by object, material, and brand, it leverages user-generated content to enhance LitterAI's predictive capabilities. While the dataset is not publicly available, the app demonstrates the potential of crowd-sourced data collection in informing waste management strategies and promoting environmental awareness.
- **Link:** [Litterati Website](https://www.litterati.org/)
