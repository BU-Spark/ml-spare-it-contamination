# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np
from collections import defaultdict, Counter
from skimage import color
from webcolors import CSS3_HEX_TO_NAMES
import matplotlib.pyplot as plt
import csv

train_path = '/home/sagemaker-user/datasets/train/images'
val_path = '/home/sagemaker-user/datasets/val/images'

import os

def get_image_paths_and_classes(images_dir, labels_dir):
    image_paths = []
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.JPG']
    for image_file in os.listdir(images_dir):
        if image_file.endswith(tuple(image_extensions)):
            base_filename = os.path.splitext(image_file)[0]
            label_file = base_filename + '.txt'
            label_path = os.path.join(labels_dir, label_file)
            image_path = os.path.join(images_dir, image_file)
            if os.path.exists(label_path):
                # Read the label file to get class IDs
                with open(label_path, 'r') as f:
                    lines = f.readlines()
                    class_ids = []
                    for line in lines:
                        tokens = line.strip().split()
                        if len(tokens):
                            class_id = int(tokens[0])
                            class_ids.append(class_id)
                    if class_ids:
                        # For simplicity, use the first class_id
                        # If you want to handle multiple classes per image, you can adjust this
                        image_paths.append((image_path, class_ids[0]))
                    else:
                        print(f"Warning: No class IDs found in label file {label_file}")
            else:
                print(f"Warning: Label file {label_file} does not exist for image {image_file}")
    return image_paths
    
train_images_dir = '/home/sagemaker-user/datasets/train/images'
train_labels_dir = '/home/sagemaker-user/datasets/train/labels'

val_images_dir = '/home/sagemaker-user/datasets/val/images'
val_labels_dir = '/home/sagemaker-user/datasets/val/labels'

train_images = get_image_paths_and_classes(train_images_dir, train_labels_dir)
val_images = get_image_paths_and_classes(val_images_dir, val_labels_dir)
all_images = train_images + val_images

# Full Dictionary with color data for objects
color_to_object = {}

# Invert the 'classes' dict to get class names to IDs
class_names_to_id = {v: k for k, v in classes.items()}


# Full dict with all classes
classes = {
    0: "Paper Cup", 1: "Snack or Candy Bag or Wrapper", 2: "Wipe", 3: "Wax Paper", 4: "Latex Gloves",
    5: "Juice or Other Pouch", 6: "Diaper", 7: "Padded Envelope (mixed materials)", 8: "Blister Pack",
    9: "Pens and Pencils", 10: "Miscellaneous Office Supplies", 11: "Facemask and Other PPE",
    12: "Shelf Stable Carton", 13: "Soiled Plastic", 14: "Soiled Metal", 15: "Soiled Glass",
    16: "Compostable Fiber Ware", 17: "Compostable Cutlery", 18: "Compostable Plastic Cups",
    19: "Compostable Paper Cups", 20: "Paper Towel/Napkins/Tissue/Tissue Paper",
    21: "Wooden Coffee Stirrer or Utensil or Chopstick", 22: "Soiled Cardboard Box",
    23: "Compostable Plastic Lid", 24: "Food Soiled Paper", 25: "Plastic strapping", 26: "Batteries",
    27: "Cables", 28: "Computers", 29: "Monitors", 30: "Toner and Ink Cartridges",
    31: "Miscellaneous Electronics", 32: "LED Lightbulb", 33: "Meat and Fish", 34: "Bones and Shells",
    35: "Cheese and Other Fats", 36: "Fruits And Veggies", 37: "Other Food or Mixed Food", 38: "Breads",
    39: "Grains", 40: "Tea Bags", 41: "Coffee Grounds & Filters", 42: "Egg Shell", 43: "Glass Bottles",
    44: "Glass Jars", 45: "Broken Glass", 46: "Metal Can", 47: "Aluminum Foil", 48: "Aluminum Catering Tray",
    49: "Other Clean Metal", 50: "Aerosol Can", 51: "Metallic Bottle Cap or Lid", 52: "Metal Strapping",
    53: "Liquids", 54: "Leaves, Flowers, Grass Clippings", 55: "Office Paper", 56: "Shredded Paper",
    57: "Clean Cardboard", 58: "Refrigerated Beverage Carton", 59: "Magazines Newspaper",
    60: "Receipts and Thermal Paper", 61: "Empty Paper Bag", 62: "Cardboard Coffee Cup Sleeve",
    63: "Clean Paper Plate", 64: "Colored Memo Note", 65: "Office Folder", 66: "Paper Roll",
    67: "Plastic Drink Bottle", 68: "Plastic Milk Jug or Personal Care Bottle", 69: "Clean Plastic Film",
    70: "Yogurt Tub or Container", 71: "Expanded Polystyrene (styrofoam)", 72: "Other Clean Plastics (rigid)",
    73: "Plastic Straws", 74: "Clear Clamshell Container", 75: "Plastic Cutlery", 76: "Plastic Lid except black",
    77: "Plastic Coffee Stirrer", 78: "Clear Plastic Cup", 79: "Colored Plastic Cup", 80: "Black Plastic",
    81: "Bubble Wrap", 82: "Incandescent Lightbulbs", 83: "CFL Lightbulbs", 84: "Textiles and Clothes",
    85: "Unclassifiable", 86: "Ceramics", 87: "Filled Bag", 88: "Coffee Pod", 89: "Wrapping Paper",
    90: "Other Clean Paper", 91: "Other Clean Glass", 92: "Drinking glass or glass ovenware", 93: "Other Trash",
    94: "Flexible container lid / seal", 95: "Snack Food Canister", 96: "Other compostable material",
    97: "Sandwich paper wrapper", 98: "Hard Cover Books", 99: "Small Paper Packets", 100: "Paper Straw",
    101: "Plastic pump"
}

color_to_object= {}

def get_image_paths(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

#Calculate the dominant color with k-means clustering.
def get_dominant_color(image):

    pixels = image.reshape(-1, 3).astype(np.float32)
    _, labels, palette = cv2.kmeans(
        pixels, 1, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2),
        10, cv2.KMEANS_RANDOM_CENTERS
    )
    return tuple(map(int, palette[0]))

#Find the closest RBG color name
def closest_color(requested_color):
    min_colors = {}
    for hex_code, name in CSS3_HEX_TO_NAMES.items():
        r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (1, 3, 5))
        rd = (r - requested_color[0]) ** 2
        gd = (g - requested_color[1]) ** 2
        bd = (b - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

#Calculate the saturation and brightness of an RGB color. Potentially going to be used to determine soiling levels

def calculate_saturation_and_brightness(color_rgb):
    color_hsv = color.rgb2hsv(np.array([[color_rgb]], dtype=np.uint8) / 255.0)
    saturation = color_hsv[0][0][1] * 100
    brightness = color_hsv[0][0][2] * 100
    return saturation, brightness

#Process and store calculated and image data
def process_images(image_paths):
    for image_path, class_id in image_paths:
        class_name = classes.get(class_id, "Unknown")  # Get class name from ID
        try:
            image = cv2.imread(image_path)
            if image is None:
                print(f"Warning: Unable to read image {image_path}")
                continue
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            dominant_color = get_dominant_color(image)
            color_name_str = closest_color(dominant_color)
            saturation, brightness = calculate_saturation_and_brightness(dominant_color)

            image_name = os.path.basename(image_path)
            note = ""

            if color_name_str.lower() == "black" and brightness < 5:
                note = " *Possible black screen or improperly taken photo"

            color_to_object[(image_name, class_name)] = {
                'dominant_color': color_name_str,
                'saturation': saturation,
                'brightness': brightness,
                'note': note
            }

            print(f"Processed image: {image_path}")
            print(f"Dominant Color: {color_name_str}, Saturation: {saturation:.2f}, Brightness: {brightness:.2f}{note}")

        except Exception as e:
            print(f"Error processing image {image_path}: {e}")

def save_results_to_csv(color_to_object, filename='color_analysis_results.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Image Name', 'Class Name', 'Dominant Color', 'Saturation', 'Brightness', 'Note']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for (image_name, class_name), data in color_to_object.items():
            writer.writerow({
                'Image Name': image_name,
                'Class Name': class_name,
                'Dominant Color': data['dominant_color'],
                'Saturation': f"{data['saturation']:.2f}",
                'Brightness': f"{data['brightness']:.2f}",
                'Note': data['note']
            })

    print(f"Results saved to {filename}")

# Combine training and validation images and process
train_images = get_image_paths(train_path)
val_images = get_image_paths(val_path)
all_images = train_images + val_images

process_images(all_images)

save_results_to_csv(color_to_object)

# for key, data in color_to_object.items():
#     print(f"Object: {key}, Color: {data['dominant_color']}, Saturation: {data['saturation']:.2f}, Brightness: {data['brightness']:.2f}, Note: {data['note']}")

# Analyze the color distribution per class
# def analyze_color_distribution(color_to_object):
#     class_color_counts = defaultdict(Counter)
#     for (image_name, class_name), data in color_to_object.items():
#         class_color_counts[class_name][data['dominant_color']] += 1

#     for class_name, color_count in class_color_counts.items():
#         print(f"\nClass: {class_name}")
#         total = sum(color_count.values())
#         for color_name, count in color_count.most_common():
#             percentage = (count / total) * 100
#             print(f"Color: {color_name}, Count: {count}, Percentage: {percentage:.2f}%")

#         # Map color names to hex codes
#         color_hex_codes = []
#         for color_name in colors:
#             for hex_code, name in CSS3_HEX_TO_NAMES.items():
#                 if name == color_name:
#                     color_hex_codes.append(hex_code)
#                     break
#             else:
#                 color_hex_codes.append('#000000')  # Default to black if color not found

#         plt.figure(figsize=(8, 4))
#         plt.bar(colors, counts, color=color_hex_codes)
#         plt.title(f"Color Distribution for Class: {class_name}")
#         plt.xlabel("Colors")
#         plt.ylabel("Counts")
#         plt.xticks(rotation=45)
#         plt.tight_layout()
#         plt.show()
# analyze_color_distribution(color_to_object)

