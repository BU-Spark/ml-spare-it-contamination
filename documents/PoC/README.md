# Spare-it Proof of Concept

## Explanation

We will have several different PoCs because we are exploring slightly different areas to solve this problem.

Jason is currently focusing on developing data preparation for classification, detection, and segmentation models, with an immediate emphasis on enhancing the detection model first to raise its accuracy up to 50%.

Tessa is delving into exploring the Litterati and Taco datasets to enhance our datasets, aiming to address class imbalance issues and improve overall accuracy.

Mustafa is developing a model based on the YOLO EC model from a [research paper](https://www.mdpi.com/1424-8220/23/7/3646).

## File Explanation

- `jason-simple-setup.ipynb`: This notebook contains code for saving data from Spare-it into the `images` and `cocojson` folders. It specifically saves images that are accompanied by labels.

- `Spare-it-PoC-JasonOh.ipynb`: This notebook presents the base detection model implementation using Spare-it's custom labels with YOLOv8. Currently, it achieves an accuracy of approximately 15% to 20%. However, it is worth noting that this accuracy is primarily observed in instances where the items occur frequently.