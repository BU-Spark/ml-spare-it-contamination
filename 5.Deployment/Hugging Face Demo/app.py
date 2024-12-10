import streamlit as st
from ultralytics import YOLO
import tempfile
import pandas as pd

model = YOLO('best.pt')

st.title('Spare-it Segmentation Model')

# Performance table data
st.header("Best Model Performance")
performance_data = {
    "Class": ["Paper Towel/Napkins/Tissue Paper", "Office Paper", "Snack or Candy Bag or Wrapper", "Metal Can", "Clean Plastic Film", "Fruits And Veggies", "Clean Cardboard", "Plastic Lid except black", "Empty Paper Bag", "Other Food or Mixed Food", "Paper Cup", "Plastic Drink Bottle", "Batteries", "Plastic Straws", "Compostable Fiber Ware", "Clear Plastic Cup", "Sandwich paper wrapper", "Filled Bag", "Wooden Coffee Stirrer or Utensil or Chopstick", "Shelf Stable Carton", "Flexible container lid / seal", "Magazines/Newspaper", "Small Paper Packets", "Plastic Cutlery", "Receipts and Thermal Paper", "Aluminum Foil", "Yogurt Tub or Container", "Cardboard Coffee Cup Sleeve", "Tea Bags", "Colored Memo Note", "Clean Paper Plate", "Glass Bottles", "Metallic Bottle Cap or Lid", "Compostable Cutlery", "Wrapping Paper", "Compostable Plastic Lid", "Plastic Milk Jug or Personal Care Bottle", "Latex Gloves", "Shredded Paper", "Refrigerated Beverage Carton", "Liquids"],
    "Images": [906, 248, 870, 634, 427, 512, 304, 333, 487, 133, 215, 2655, 148, 184, 146, 86, 110, 63, 231, 30, 78, 26, 61, 22, 62, 451, 47, 32, 32, 41, 44, 49, 35, 37, 31, 32, 63, 17, 8],
    "Instances": [1870, 562, 1662, 1560, 626, 928, 573, 373, 970, 196, 355, 3553, 164, 167, 196, 94, 172, 65, 655, 112, 132, 112, 72, 18, 71, 510, 51, 33, 34, 47, 54, 59, 44, 49, 39, 39, 74, 21, 8],
    "Box(P)": [0.695, 0.652, 0.683, 0.856, 0.663, 0.71, 0.685, 0.675, 0.671, 0.628, 0.687, 0.835, 0.704, 0.747, 0.666, 0.704, 0.649, 0.705, 0.695, 0.585, 0.662, 0.643, 0.615, 0.601, 0.542, 0.757, 0.556, 0.283, 0.431, 0.326, 0.344, 0.451, 0.503, 0.354, 0.515, 0.662, 0.546, 0.603, 0.777, 0.954],
    "Box(R)": [0.665, 0.58, 0.623, 0.922, 0.482, 0.607, 0.621, 0.589, 0.591, 0.421, 0.738, 0.859, 0.729, 0.729, 0.667, 0.682, 0.549, 0.566, 0.611, 0.463, 0.533, 0.633, 0.515, 0.507, 0.351, 0.705, 0.474, 0.354, 0.329, 0.305, 0.256, 0.617, 0.543, 0.433, 0.568, 0.617, 0.717, 0.581, 0.567, 0.357],
    "Box(mAP50)": [0.726, 0.605, 0.615, 0.892, 0.542, 0.656, 0.626, 0.604, 0.597, 0.487, 0.687, 0.859, 0.729, 0.718, 0.686, 0.635, 0.569, 0.621, 0.651, 0.485, 0.584, 0.633, 0.511, 0.507, 0.384, 0.745, 0.524, 0.354, 0.321, 0.305, 0.257, 0.627, 0.444, 0.393, 0.568, 0.711, 0.467, 0.561, 0.744, 0.123],
    "Mask(mAP50-95)": [0.462, 0.357, 0.411, 0.683, 0.314, 0.453, 0.391, 0.372, 0.367, 0.268, 0.437, 0.737, 0.523, 0.483, 0.437, 0.373, 0.318, 0.428, 0.435, 0.365, 0.385, 0.421, 0.321, 0.358, 0.283, 0.619, 0.351, 0.234, 0.212, 0.189, 0.147, 0.392, 0.318, 0.27, 0.391, 0.492, 0.248, 0.318, 0.587, 0.118],
}

df = pd.read_csv('performance_table.csv')
st.dataframe(df)

with st.expander("See Example Results"):
    st.write("Here are some example images with detections:")
    st.image('example1.jpg')
    st.image('example2.jpg')
    st.image('example3.jpg')
    st.image('example4.jpg')
    st.image('example5.jpg')


input_method = st.radio("Choose the input method:", ("Upload an Image", "Take a Picture"))

if input_method == "Upload an Image":
    image_data = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

elif input_method == "Take a Picture":
    image_data = st.camera_input("Take a picture")

if image_data is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
        tmp_file.write(image_data.getvalue())
        image_path = tmp_file.name

    results = model(image_path)

    category_names = results[0].names 

    predictions = {}
    for cls_id, conf in zip(results[0].boxes.cls, results[0].boxes.conf):
        cls_id = int(cls_id)
        conf = float(conf)
        class_name = category_names[cls_id]
        if class_name in predictions:
            predictions[class_name].append(conf)
        else:
            predictions[class_name] = [conf]

    num_masks = len(results[0].masks.data)

    st.write(f"Total {num_masks} objects found.")
    for category, confidences in predictions.items():
        st.write(f"{len(confidences)} {category}: {['{:.2f}'.format(c) for c in confidences]}")

    for result in results:
        plotted_img = result.plot()
        st.image(plotted_img, caption='Segmented Image', use_container_width =True)
