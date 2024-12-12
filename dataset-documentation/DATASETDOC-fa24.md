***Project Information*** 

* What is the project name?  
  * Spare-it: Contamination Identification 
* What is the link to your project’s GitHub repository?   
  * https://github.com/BU-Spark/ml-spare-it-contamination/tree/main
* What is the link to your project’s Google Drive folder? \*\**This should be a Spark\! Owned Google Drive folder \- please contact your PM if you do not have access\*\**  
  *   https://drive.google.com/drive/folders/1Dl7l3p843Wh7pH4EtRpJOnboXs-ZhLsU?usp=drive_link
* In your own words, what is this project about? What is the goal of this project?   
  * This project is about developing a machine learning model capable of predicting contamination and identifying missed opportunities for recycling and waste management. The goal is to reduce waste contamination and increase sustainabilty. 
* Who is the client for the project?  
  * Spare-it
* Who are the client contacts for the project?  
  *  Laurent Meunier: laurent.meunier@spare-it.com 
  * Jason Oh: jason.oh@spare-it.com
* What class was this project part of?  
  * DS549

***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  
  * SCC path: /projectnb/ds549/datasets/spare-it
* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project. 
  * copy-paste: A dataset of Spare-it images augmented with copy-paste 
  * original_dataset: A dataset containing the original Spare-it images
  * taco_transformed: A dataset containing TACO images transformed to Spare-it format
* What keywords or tags would you attach to the data set?  
  * Domain(s) of Application: Computer Vision, Object Detection, OCR, Image Classification, Image Segmentation, Facial Recognition, NLP, Topic Modeling, Sentiment Analysis, Named Entity Recognition, Text Classification, Summarization, Anomaly Detection, Other   
    * Computer Vision 
    * Image Segmentation 
  * Sustainability, Health, Civic Tech, Voting, Housing, Policing, Budget, Education, Transportation, etc.   
    * Sustainability 

*The following questions pertain to the datasets you used in your project.*   
*Motivation* 

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.   
  * The main purpose for creating the dataset was to be able to train a segmentation model to identify contamination in trash. This is will help to fill the gap around workspace waste management.

*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.   
  * The instances of the dataset are images of trash along with corresponding segmentation masks 
* How many instances are there in total (of each type, if appropriate)?  
  * There are around 18k instances of images.
* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).  
  * The dataset is a sample as it only contains images of trash from certain buildings/organizations. This my not be representative of the larger set but this is justified because it should generalize to images of trash in other buildings as the images will still look similar and the classification is comprehensive.  
* What data does each instance represent? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.   
  * Each data instance is an image of a trash/recycling/compost bin 
* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.   
  * No information missing.  
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them  
  * We use a traditional 80-20 train-val split. The only challenge is to ensure all of the types of trash are well represented in the validation data. 
* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.   
  * None - the dataset is very high quality. 
* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,   
  * The original Spare-it dataset is self-contained.   
* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.   
  * No, the data is just images of waste.
* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.   
  *  No, the data is just images of waste.
* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.   
  * The dataset may include PII in the form of Grubhub receipts etc. but it is highly unlikely.  
* Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset. 


| Size of dataset | ~25 GB |
| :---- | :---- |
| Number of instances | 18,169 |
| Number of fields  | N/A |
| Labeled classes (for classification tasks) | 130 |
| Number of labels (for classification tasks) | ~150k |


  
*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?  
  * The data was collected by students taking pictures of trash. 
* If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?  
  * The dataset we used was provided to us. The client should be contacted to discuss if it is sampled from a larger set and how it was chosen. 
* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.   
  * Contact the client for the exact timeframe, but we believe the data was collected within the past couple years. 

*Preprocessing/cleaning/labeling* 

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.   
  * No preprocessing/cleaning/labeling or altering of the dataset. It is given in standard COCO JSON format. 
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.   
  * For model training, we cropped out the background of the images using the segmentation masks.   
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.  
  * Yes the raw data is still the same and can be found in the SCC at: /projectnb/ds549/datasets/spare-it/original_dataset
* Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository).   
  * https://github.com/BU-Spark/ml-spare-it-contamination/blob/dev/4.POC/spare-it-segmentation-model.ipynb

*Uses* 

* What tasks has the dataset been used for so far? Please provide a description.   
  * The dataset has been used to train a segmentation model.
* What (other) tasks or applications could the dataset be used for? 
  * The dataset can also be used for training an object detection model.
* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?   
  * We do not forsee anything that would impact future uses.
* Are there tasks for which the dataset should not be used? If so, please provide a description.  
  * None.

*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?  
  * Internal: The dataset is Spare-it proprietary data. 

*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description or a link to the code.  
  * Yes, others can contact Spare-it if they would like to contribute to the dataset. 

*Other*

* Is there any other additional information that you would like to provide that has not already been covered in other sections?  
  * None.

