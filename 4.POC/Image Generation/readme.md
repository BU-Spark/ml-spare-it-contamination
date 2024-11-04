## AI-Image Generation

### Overview

As per the tasks in the project description, we have tried to generate images as an effort to enhance the underrepresented calsees in their dataset. We tried to train both a  GAN and a diffusion model, but results were sub-optimal likely due to the lack of training data. We then tried to fine-tune a pretrained stable diffusion model on the Spare-it dataset and generate images for a specific class (teabags), which yielded better results as shown below. 

### File directory

- **`diffusion_tuning.ipynb`**: This notebook contains the code that we used to fine-tune stable diffusion. 
- **`Image_Cropper.ipynb`**: This notebook contains code to extract images for a give label from the Spare-it dataset using the segmentation masks. 

### Results

#### Sample of teabags in Spare-it dataset:

![image](https://github.com/user-attachments/assets/00011948-3421-43a0-bacd-e1fad5ffce5d)

#### Sample of generated images:

![generated_image_0 (3)](https://github.com/user-attachments/assets/40822dce-1e68-4f62-8a59-c46ba0c455d8)
![generated_image_0 (4)](https://github.com/user-attachments/assets/14699f2e-ee56-443f-a85c-6510f2577a79)
![generated_image_2](https://github.com/user-attachments/assets/47227a8f-f454-414d-a1d7-2bd821b7293b)
![generated_image_0](https://github.com/user-attachments/assets/faaa6c58-bb14-4100-bfa6-a885d6b0aaba)
![generated_image_4 (2)](https://github.com/user-attachments/assets/b112aba5-0825-4e45-8bca-e1f082690d83)

This exercise also revealed a potential issue regarding how the Spare-it data is labeled. As shown above, some of the teabags in the Spare-it dataset are just paper tags. This might confuse the segmentation model just like how it sometimes confused the diffusion model. For example, here is a generated image that resembles a paper tag:

![generated_image_0](https://github.com/user-attachments/assets/192b9c16-4738-44b2-9d1f-94e85d3ce9a8)
