import streamlit as st
from ultralytics import YOLO
import tempfile


model = YOLO('best.pt')

st.title('Spare-it Segmentation Model')

with st.expander("See Example Results"):
    st.write("Here are some example images with detections:")
    st.image('exampeimg1.jpg')
    st.image('exampeimg2.png')
    st.image('exampeimg3.jpg')
    st.image('exampeimg4.jpg')
    st.image('exampeimg5_original.jpeg')
    st.image('exampeimg5.jpg')


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
