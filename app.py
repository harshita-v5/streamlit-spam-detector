import streamlit as st
import joblib
model = joblib.load("spam_classifier_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="centered")

st.header("Email Spam Detector")

st.subheader("Enter an email message below to check if it's spam or not.")

email=st.text_area("Email content", height=200, placeholder="Type or paste your email content here...")


if st.button("Check if Spam"):
    if email.strip() == "":
        st.warning("Please enter some email content!")
    else:
       
        vect_email = vectorizer.transform([email])
        prediction = model.predict(vect_email)

        
        if prediction[0] == 1:
            st.error("🚨 This email is **SPAM**!")
        else:
            st.success("✅ This email is **HAM** (Not Spam).")