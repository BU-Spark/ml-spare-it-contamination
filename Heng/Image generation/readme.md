Per client request, We have tried to generate images as an effort to enhance the underrepresented calsees in their dataset. We tried to train a Gan and a diffusor, which both faield to convered, likely due to the lack of training data. We then tried to fine-tune a pretrained stable diffusion model on spare-it dataset and make it generate image for a specific class(teabags), which showed some success.

sample of teabags in spare-it dataset:
![image](https://github.com/user-attachments/assets/00011948-3421-43a0-bacd-e1fad5ffce5d)






sample of enerated images:

![generated_image_0 (3)](https://github.com/user-attachments/assets/40822dce-1e68-4f62-8a59-c46ba0c455d8)
![generated_image_0 (4)](https://github.com/user-attachments/assets/14699f2e-ee56-443f-a85c-6510f2577a79)
![generated_image_2](https://github.com/user-attachments/assets/47227a8f-f454-414d-a1d7-2bd821b7293b)
![generated_image_0](https://github.com/user-attachments/assets/faaa6c58-bb14-4100-bfa6-a885d6b0aaba)
![generated_image_4 (2)](https://github.com/user-attachments/assets/b112aba5-0825-4e45-8bca-e1f082690d83)


This exercise also revealed a potential issue regarding how the spare-it is labeled: As shown in the [sample of teabags in spare-it dataset], some of the images are mere paper tags. This might confuse the segmentation/identification model just like how it sometimes confused the diffusion model: 

![generated_image_0](https://github.com/user-attachments/assets/192b9c16-4738-44b2-9d1f-94e85d3ce9a8)
