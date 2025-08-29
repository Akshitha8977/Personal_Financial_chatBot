
import streamlit as st
import os
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import Model
from transformers import pipeline
from dotenv import load_dotenv

# Load .env from same directory as app.py
load_dotenv()



# Sentiment Analysis using Hugging Face Transformers
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_query(query):
    result = classifier(query)
    return result[0]['label']

import matplotlib.pyplot as plt

# ----------------- IBM Setup -----------------
API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
BASE_URL = os.getenv("WATSONX_URL")

creds = Credentials(api_key=API_KEY, url=BASE_URL)

model = Model(
    model_id="ibm/granite-13b-instruct-v2",
    credentials=creds,
    project_id=PROJECT_ID,
    params={"max_new_tokens": 200, "temperature": 0.2}
)

def ask_granite(prompt):
    resp = model.generate(prompt=prompt)
    return resp["results"][0]["generated_text"]

# ----------------- Hugging Face -----------------
classifier = pipeline("text-classification", 
                      model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_query(query):
    return classifier(query)[0]['label']

# ----------------- Finance Logic -----------------
def calculate_savings(income, expenses):
    return income - expenses

def tax_advice(income):
    if income < 500000:
        return "No tax applicable. Save via SIP or FD."
    elif income < 1000000:
        return "20% tax. Use 80C deductions (PPF, ELSS, LIC)."
    else:
        return "30% tax. Use ELSS, NPS, and advanced planning."

def investment_suggestions(profile):
    if profile == "Student":
        return "SIPs, RD, Index Funds."
    else:
        return "Mutual funds, ELSS, NPS, SIPs."

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="💰 Finance Chatbot", layout="wide")

st.title("💰 Personal Finance Chatbot")

user_type = st.sidebar.selectbox("Profile", ["Student", "Professional"])
income = st.sidebar.number_input("Monthly Income (₹)", min_value=1000, step=500)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=500, step=100)

query = st.text_input("Ask about savings, taxes, or investments:")

if st.button("Get Advice"):
    # Savings
    savings = calculate_savings(income, expenses)
    st.write(f"✅ Your monthly savings: ₹{savings}")

    # Rule-based advice
    if "tax" in query.lower():
        st.info(tax_advice(income))
    elif "invest" in query.lower():
        st.info(investment_suggestions(user_type))
    else:
        st.warning("I can advise on savings, taxes, and investments.")

    # Hugging Face intent
    intent = classify_query(query)
    st.write(f"📌 Detected intent: {intent}")

    # Granite AI
    granite_ans = ask_granite(query)
    st.success(f"🔮 Granite: {granite_ans}")

    # Visualization
    categories = ["Rent", "Food", "Transport", "Entertainment", "Other"]
    values = [15000, 8000, 3000, 4000, 2000]

    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, autopct="%1.1f%%")
    st.pyplot(fig)
