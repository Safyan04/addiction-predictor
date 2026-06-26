import streamlit as st
import joblib
import pandas as pd

# Model load karein
model = joblib.load('addiction_model.pkl')

st.title("📱 Social Media Addiction Predictor")

# Saari default values 0 set kar di gayi hain
age = st.number_input("Age", 0, 100, 0)
daily_screen_time = st.number_input("Daily Screen Time", 0.0, 24.0, 0.0)
social_media_hours = st.number_input("Social Media Hours", 0.0, 24.0, 0.0)
study_hours = st.number_input("Study Hours", 0.0, 24.0, 0.0)
sleep_hours = st.number_input("Sleep Hours", 0.0, 24.0, 0.0)
notifications_per_day = st.number_input("Notifications per Day", 0, 1000, 0)
focus_score = st.number_input("Focus Score", 0.0, 100.0, 0.0)
productivity_score = st.number_input("Productivity Score", 0.0, 100.0, 0.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'age': [age],
        'daily_screen_time': [daily_screen_time],
        'social_media_hours': [social_media_hours],
        'study_hours': [study_hours],
        'sleep_hours': [sleep_hours],
        'notifications_per_day': [notifications_per_day],
        'focus_score': [focus_score],
        'productivity_score': [productivity_score]
    })
    
    # Model seedha labels ('High', 'Low', 'Medium') return kar raha hai
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Addiction Level: {prediction[0]}")