import streamlit as st
from ultralytics import YOLO
import tempfile
import pandas as pd

# Load the model
model = YOLO('best.pt')

st.title('Spare-it Recyclable Detection Model')

st.write("""
This detection model is designed to identify recyclable items within images, providing high detection capabilities across 20 categories. Below are the performance metrics for specific recyclable materials.
""")

with st.expander("See Example Results"):
    st.write("Here are some example images with detections:")
    st.image('result1.jpg')
    st.image('result2.jpg')
    st.image('result3.jpg')
    st.image('result4.jpg')
    st.image('result5.jpg')
    st.image('result6.jpg')

# Hardcoded table with performance metrics
data = {
    'Category': [
        'Overall', 'Shredded Paper', 'Metal Can', 'Aluminum Foil', 'Paper Cup',
        'Office Paper', 'Paper Towel/Napkins/Tissue', 'Glass Bottles', 'Plastic Drink Bottle',
        'Compostable Fiber Ware', 'Fruits And Veggies', 'Clear Plastic Cup', 'Black Plastic',
        'Cardboard Coffee Cup Sleeve', 'Snack or Candy Bag or Wrapper', 'Plastic Lid except black',
        'Filled Bag', 'Empty Plastic Bag', 'Clean Paper Plate', 'Shelf Stable Carton',
        'Clean Cardboard', 'Empty Paper Bag'
    ],
    'Total Images': [1667] * 22,
    'Samples': [12871, 16, 1227, 58, 405, 1588, 4304, 58, 378, 244, 635, 245, 136, 74, 1018, 509, 287, 529, 43, 134, 587, 396],
    'Precision': [0.527, 0.845, 0.79, 0.674, 0.607, 0.564, 0.562, 0.562, 0.559, 0.52, 0.518, 0.513, 0.469, 0.467, 0.462, 0.459, 0.428, 0.422, 0.416, 0.414, 0.41, 0.402],
    'Recall': [0.451, 0.5, 0.801, 0.414, 0.568, 0.409, 0.518, 0.5, 0.574, 0.623, 0.378, 0.551, 0.485, 0.343, 0.333, 0.344, 0.37, 0.308, 0.256, 0.396, 0.419, 0.371],
    'mAP50': [0.448, 0.5, 0.855, 0.434, 0.595, 0.437, 0.533, 0.511, 0.578, 0.593, 0.377, 0.465, 0.479, 0.363, 0.339, 0.321, 0.37, 0.279, 0.275, 0.433, 0.35, 0.328],
    'mAP50-95': [0.315, 0.429, 0.667, 0.307, 0.44, 0.272, 0.315, 0.298, 0.386, 0.489, 0.23, 0.331, 0.367, 0.244, 0.211, 0.232, 0.248, 0.158, 0.232, 0.296, 0.256, 0.215]
}
df = pd.DataFrame(data)

st.dataframe(df, hide_index=True)

input_method = st.radio("Choose the input method:", ("Upload an Image", "Take a Picture"))

if input_method == "Upload an Image":
    image_data = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

elif input_method == "Take a Picture":
    image_data = st.camera_input("Take a picture")

if image_data is not None:
    # make temp image file to run detection
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
        tmp_file.write(image_data.getvalue())
        image_path = tmp_file.name

    results = model(image_path)

    category_names = results[0].names
    predictions = {}
    for box in results[0].boxes:
        cls_id = int(box.cls)
        conf = float(box.conf)
        if cls_id in category_names:
            if category_names[cls_id] in predictions:
                predictions[category_names[cls_id]].append(conf)
            else:
                predictions[category_names[cls_id]] = [conf]

    st.write(f"Total {len(results[0].boxes.cls)} objects found.")
    for category, confidences in predictions.items():
        st.write(f"{len(confidences)} {category}: {['{:.2f}'.format(c) for c in confidences]}")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as output_tmp:
        for result in results:
            result.save(filename=output_tmp.name)
        st.image(output_tmp.name, caption='Predicted Image', use_column_width=True)