"""A small Streamlit app for diabetes-risk predictions."""

import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = "models/diabetes_model.pkl"


@st.cache_resource
def load_model():
    """Load the trained model once, then keep it in Streamlit's cache."""
    return joblib.load(MODEL_PATH)


def create_input_data(gender, age, hypertension, heart_disease,
                      smoking_history, bmi, hba1c_level, blood_glucose_level):
    """Put the form values into the same column layout used for training."""
    return pd.DataFrame(
        {
            "gender": [gender],
            "age": [age],
            "hypertension": [hypertension],
            "heart_disease": [heart_disease],
            "smoking_history": [smoking_history],
            "bmi": [bmi],
            "HbA1c_level": [hba1c_level],
            "blood_glucose_level": [blood_glucose_level],
        }
    )


st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺")
st.title("🩺 Diabetes Risk Predictor")
st.write("Enter health information to get a prediction from a Random Forest model.")

try:
    model = load_model()
except (FileNotFoundError, EOFError):
    st.error("A trained model was not found. Run `03_Model_Training.ipynb` first.")
    st.stop()

with st.form("prediction_form"):
    left_column, right_column = st.columns(2)

    with left_column:
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
        age = st.number_input("Age", min_value=0.0, max_value=120.0, value=30.0, step=1.0)
        bmi = st.number_input("BMI", min_value=10.0, max_value=80.0, value=25.0, step=0.1)
        hba1c_level = st.number_input(
            "HbA1c level", min_value=3.0, max_value=15.0, value=5.5, step=0.1
        )

    with right_column:
        hypertension = st.selectbox("Hypertension", [0, 1], format_func=lambda value: "Yes" if value else "No")
        heart_disease = st.selectbox("Heart disease", [0, 1], format_func=lambda value: "Yes" if value else "No")
        smoking_history = st.selectbox(
            "Smoking history",
            ["No Info", "never", "former", "current", "ever", "not current"],
        )
        blood_glucose_level = st.number_input(
            "Blood glucose level", min_value=50, max_value=400, value=100, step=1
        )

    submitted = st.form_submit_button("Predict risk")

if submitted:
    input_data = create_input_data(
        gender, age, hypertension, heart_disease, smoking_history,
        bmi, hba1c_level, blood_glucose_level,
    )

    # predict_proba gives the probability for each class: [no diabetes, diabetes].
    diabetes_probability = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction")
    if prediction == 1:
        st.warning("The model predicts a higher likelihood of diabetes.")
    else:
        st.success("The model predicts a lower likelihood of diabetes.")

    st.metric("Estimated probability", f"{diabetes_probability:.1%}")
    st.caption(
        "This is an educational machine-learning project, not medical advice. "
        "Please speak to a qualified healthcare professional about medical concerns."
    )
