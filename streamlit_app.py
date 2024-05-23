import streamlit as st
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and vectorizer
model_path = 'pkl_file.py'
vectorizer_path = 'vectorizer.pkl'

with open(model_path, 'rb') as file:
    model = pickle.load(file)

with open(vectorizer_path, 'rb') as file:
    vectorizer = pickle.load(file)

def extract_features(url):
    # Example feature extraction (customize based on your actual feature extraction)
    data = pd.DataFrame([url], columns=['url'])
    features = vectorizer.transform(data['url'])
    return features

def main():
    st.title("Phishing URL Detection")
    st.write("Enter a URL to check if it is phishing or not.")

    url_input = st.text_input("URL")

    if st.button("Detect"):
        if url_input:
            features = extract_features(url_input)
            prediction = model.predict(features)
            prediction_proba = model.predict_proba(features)

            if prediction[0] == 1:
                st.error("The URL is likely a phishing URL.")
            else:
                st.success("The URL is likely safe.")

            st.write("Prediction Probability: ", prediction_proba)
        else:
            st.warning("Please enter a URL.")

if __name__ == "__main__":
    main()




   

   



