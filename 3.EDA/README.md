# Spare-it Exploratory Data Analysis (EDA)

We have provided a Jupyter Notebook for our Exploratory Data Analysis.

## Extra Setup

You don't need to install any external libraries. To use the notebook, ensure that you have an `images-and-labels` folder in the same directory as the notebook, containing all your images and labels data.

However, you can also run this inside the Google Colab environment. To do so, you can add a Google Drive connection code snippet and change the file directory accordingly, as shown below:

```python
from google.colab import drive
drive.mount('/content/drive')
folder_path = '/content/drive/MyDrive/{path/to/data}'
```

Place the above code snippet at the top of your notebook to access the dataset from your Google Drive.