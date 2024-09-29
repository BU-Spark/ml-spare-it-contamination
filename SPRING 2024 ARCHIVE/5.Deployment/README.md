# Spare-it Model Deployment Guide

## General Info

We are using Streamlit and Ultralytics YOLOv8 to create a quick demo for our model. If you need to build a mobile application, Streamlit does not support that. You will have to use Flask or FastAPI for the backend and Flutter or Expo/React Native for the frontend to create a demo.

Important thing to note for first-time Streamlit users is that when you pass file data, it changes into a "file-like" format, so you have to use methods like `.getvalue()` for images. Additionally, Streamlit does not cache images, so you need to use `tempfile` to cache it yourself.

## Installation

1. Ensure you have the `best.pt` or any `.pt` file in the same directory as your project.

2. Generate a virtual environment named `venv` or `env` using the following command:
   ```
   python -m venv venv
   ```

3. Install the essential packages by running:
   ```
   pip install -r requirements.txt
   ```

4. Start your application by running:
   ```
   streamlit run your_script_name.py
   ```

## Deployment

1. Create a Hugging Face account if you don't have one already.

2. Deploy the application to Hugging Face. This process is very similar to how you upload files to GitHub. Follow the Hugging Face documentation for detailed instructions on deployment.