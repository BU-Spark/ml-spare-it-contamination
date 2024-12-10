## AI-Image Generation

### Overview

As per the tasks in the project description, we have tried to generate synthetic images in an effort to augment the underrepresented classes in the Spare-it dataset. We tried to train both a GAN and a diffusion model, but results were sub-optimal likely due to the lack of training data. We then tried to fine-tune a pretrained stable diffusion model on the Spare-it dataset and generate images for a single class, which yielded better results. We believe this can be potentially be very useful in augmenting the underrepresented classes and diversifying the dataset for training, so we have established a ready-to-use pipeline to fine-tune the stable diffusion model on any classes in the Spare-it dataset. As an example usage, the results are shown below for teabags, latex gloves, and shredded paper.

### File directory

- **`Image_Extractor.ipynb`**: This notebook contains code to extract images for given labels from the Spare-it dataset using the segmentation masks. 
- **`Training_pipeline.ipynb`**: This notebook contains the pipeline we built for fine-tuning stable diffusion. Currently, the notebook only saves the fine-tuned Unet and use the base model's encoder for generation. It is recommended to save the entire model instead if your hardware capacity allows that.

#### Sample of generated images:

![generated_image_0 (4)](https://github.com/user-attachments/assets/14699f2e-ee56-443f-a85c-6510f2577a79)
![generated_image_0](https://github.com/user-attachments/assets/faaa6c58-bb14-4100-bfa6-a885d6b0aaba)
![image](https://github.com/user-attachments/assets/0114727a-f45c-47a2-916d-3daf889ed14f)
![generated_6](https://github.com/user-attachments/assets/2f26b2d0-9409-46d9-8593-cbefce666675)
![generated_6_0](https://github.com/user-attachments/assets/47055a34-4f59-4405-bcd3-0d22ff7973c8)
![generated_6_1](https://github.com/user-attachments/assets/5da5de06-1ea9-4f50-a935-ea249b38968c)
![generated_77](https://github.com/user-attachments/assets/50cf239e-c96c-44a5-a421-a49dc705fe8c)
![generated_77_0](https://github.com/user-attachments/assets/f31b4955-cc21-43f3-a06e-4912d3c84e32)
![generated_77_1](https://github.com/user-attachments/assets/d7a03ec4-d61f-4ad1-a820-e1a4d4c620bd)
