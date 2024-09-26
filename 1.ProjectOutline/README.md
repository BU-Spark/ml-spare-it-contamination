` # Technical Project Document Template

## Tia Hannah, Devon Solheim, Heng Chang, Arjun Chandra, 2024-09-26 v2.0.0-dev

## Overview

Spare-it aims to empower businesses, office owners, and universities with the ability to monitor and reduce various types of workspace waste effectively. The project's core objective is to develop a machine learning model that can autonomously identify contamination and missed recycling opportunities by analyzing images of waste bins. This technology seeks to enhance sustainability efforts by providing actionable insights into waste management practices, thus facilitating a more environmentally friendly and efficient approach to handling waste and recyclables.

### A. Provide a solution in terms of human actions to confirm if the task is within the scope of automation through AI.

Human actions involved in identifying contamination and missed opportunities in recycling include:

- **Visual Inspection:** A person would examine images of waste bins to identify recyclable materials incorrectly disposed of as general waste or contaminants within the recycling stream.
- **Classification:** Based on the visual inspection, the person categorizes each image as either 'Contaminated' or a 'Missed Opportunity' for recycling.
- **Data Recording:** The findings from the inspection and classification are then recorded, potentially in a database, for further analysis or action.

This process aligns well with automation through AI, as machine learning models can be trained to replicate these human actions with high efficiency and scalability. AI can continuously analyze large volumes of images, providing real-time insights and recommendations for improving waste sorting practices.

### B. Problem Statement:
The project focuses on creating a machine learning model capable of predicting contamination levels and identifying missed opportunities for recycling through the analysis of waste bin images. This involves distinguishing between general waste, recyclables, electronics, and other waste types to improve waste sorting and reduce contamination. The challenge lies in accurately classifying images into categories of 'Contaminated' or 'Missed Opportunity' based on the presence of specific objects and materials that should have been recycled or disposed of differently. This can be formulated as a machine learning problem in different ways, but based on the previous semesters’ work, it is being treated as an object detection problem which involves both localization and classification. 


### C. Checklist for project completion

- [x]  Label Data Optimization and External Dataset Analysis:  Refine labeled data by splitting complex classes and find external datasets and analyze them for better classification.
 
- [x] Data Pipeline Enhancement: Create a scalable and optimized live data pipeline to incorporate external datasets and live data.

- [x] AI Image Generation Exploration: Implement advanced image AI models to generate high-quality synthetic images for testing and for easier classification of the real images (Flux 1, SAM)

- [x] ML Pipeline Enhancements: Research and use open-source tools to improve precision and mAP values in segmentation models, focusing on the accuracy of classification.

- [x] Front-End Enhancement: Host and Update the front-end platform to both be more user-friendly and  reflect the improved data labeling and AI image generation features. 


### D. Outline a path to operationalization.

1. **Improve the AI Model:** Improve the previous machine learning model to more accuratelyidentify contamination and missed recycling opportunities from images of waste bins.
2. **Refine the User Interface:** Refine the interface where users can upload images of waste bins for analysis.
3. **Deploy the Model:** Host the AI model on a cloud platform to analyze images uploaded by users in real time.
4. **Provide Feedback:** Automatically generate and display feedback on waste sorting to the user based on the AI analysis.
5. **Collect Data:** Use the data from user uploads to continuously improve the AI model's accuracy.
6. **Launch a Pilot Program:** Test the system with a limited user group to gather feedback and make necessary adjustments.
7. **Official Release:** Roll out the application for wider use with full functionality and support.

This approach focuses on developing and deploying the core functionalities needed to bring the Spare-it project to its users, with an emphasis on simplicity and effectiveness.


## Resources
- [YOLOv8 by Ultralytics](https://docs.ultralytics.com/tasks/segment/)
- [Segment Anything (SAM) by Meta](https://segment-anything.com/)
- [Black Forest Labs (Flux.1)](https://huggingface.co/black-forest-labs)
- [This is how images are classified and labeled](https://www.google.com/url?q=https://airtable.com/appfD0HATg3Ii35Oo/shrN7ywJvqfJV3ROE/tblEaPEKrbEVOeHic&sa=D&source=docs&ust=1727381391761009&usg=AOvVaw2CL2OQTQsYEj4lrWrI1g-m)

### Data Sets
- https://drive.google.com/drive/u/1/folders/1rGmiwSvCddAuQlnnxbJiIE8sJdiSvIY3
- Processed 4,640 images and labels from a total dataset of 29,000, using a taxonomy of 102 specific objects for detailed waste classification.
- Researched External sources/datasets
- Synthetic/ AI-generated Images

## Weekly Meeting Updates
