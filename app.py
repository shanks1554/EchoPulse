import streamlit as st
import joblib

# Load the trained pipeline and label encoder
model = joblib.load("models/classifier.joblib")
label_encoder = joblib.load("models/LabelEncoder.joblib")

# Streamlit UI
st.set_page_config(page_title="Tweet Sentiment Analyzer", layout="centered")
st.title("Tweet Sentiment Analysis")
st.markdown("Enter a tweet below to analyze its sentiment.")

# Input field
tweet_text = st.text_area("Tweet Text", height=150)

# Predict button
if st.button("Analyze Sentiment"):
    if tweet_text.strip() == "":
        st.warning("Please enter a tweet text.")
    else:
        # Predict numeric label
        pred_num = model.predict([tweet_text])[0]
        
        # Convert number to original label
        pred_label = label_encoder.inverse_transform([pred_num])[0]
        
        # Display result
        st.success(f"Predicted Sentiment: **{pred_label}**")
