# Spare-it Proof of Concept (PoC)

This directory contains our Proof of Concept. We have outlined all the steps taken to generate our base model for Spare-it's recyclable detection.

## File Directory

- `Spare-it-PoC.ipynb`: Contains all the code needed to generate our model.

- `dataset-top20-recall.yaml`, `dataset-top20-count.yaml`, `dataset.yaml`, `best.pt`: These are some files needed to test out all codes in the notebook.

- `./DCGAN`: Contains the DCGAN implementation for generating recyclable photos, which is important for enhancing our dataset through data augmentation.

## Overview

Our end result was 52.7% accuracy for 20 selected class labels out of 100. We started with 100 labels, but some labels didn't occur or had very few occurrences, which negatively impacted the model. Therefore, through discussions with Spare-it, we decided to generate a model with a smaller label set to evaluate accuracy and identify future improvements. Detailed, step-by-step information is provided in the Jupyter notebook.

As the DCGAN feature was built on the side, we have not implemented it with our current model.

## Key Findings and Improvements

1. Most importantly, figuring out why some labels, like "Unclassifiable" or "Other Clean Plastics (rigid)", have a low recall rate despite having many occurrences will be key to improving the model.

2. We performed moderate data augmentation; applying more extensive augmentation could enhance accuracy.

3. Since these items are very close to each other in the image, adjusting the focal loss could potentially improve the model and reduce false positives.