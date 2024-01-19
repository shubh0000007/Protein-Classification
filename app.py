import streamlit as st
import pickle

# Title and description
st.title("Protein Sequence Predictor")
st.write("Upload a pickle file containing the model pipeline and enter a protein sequence to predict its label.")

# File upload for the pickle file
model_file = st.file_uploader("Upload your model pickle file", type=["pkl"])

# Input text box for protein sequence
input_sequence = st.text_input("Enter a protein sequence:")

# Predict button
if st.button("Predict"):
    if model_file is not None and input_sequence:
        # Load the model pipeline from the uploaded pickle file
        with model_file:
            protein_pipeline = pickle.load(model_file)

        # Predict the label using the loaded pipeline
        predicted_label = protein_pipeline.predict([input_sequence])[0]

        # Display the predicted label
        st.write("Predicted Label:", predicted_label)
    else:
        st.write("Please upload a model pickle file and enter a protein sequence.")
