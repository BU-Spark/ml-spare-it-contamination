#!/usr/bin/env python
# coding: utf-8

import json
import requests
import os

def download_images_from_json(json_path, save_folder):
    with open(json_path, 'r') as f:
        data = json.load(f)
    os.makedirs(save_folder, exist_ok=True)

    for image_info in data.get("images", []):
        url = image_info.get("flickr_url")
        file_name = image_info.get("file_name")

        if url and file_name:
            parsed_file_name = file_name.replace("/", "_")

            try:
                response = requests.get(url)
                response.raise_for_status()  


                image_path = os.path.join(save_folder, parsed_file_name)
                with open(image_path, 'wb') as img_file:
                    img_file.write(response.content)
                
                print(f"Downloaded {parsed_file_name}")

            except requests.exceptions.RequestException as e:
                print(f"Failed to download {parsed_file_name}: {e}")

# Usage example
json_path = 'taco_annotations.json'  
save_folder = 'images'   

download_images_from_json(json_path, save_folder)