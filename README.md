
# 💰 Personal Finance Chatbot

A simple AI-powered chatbot that helps users manage their personal finances by providing **budget planning, savings advice, tax tips, and investment suggestions**. The chatbot combines **rule-based logic** with **AI models (IBM WatsonX + Hugging Face)** and a **Streamlit interface** for easy interaction.

---

## 🚀 Features

* ✅ Budget calculation (savings, expenses)
* ✅ Tax advice based on income levels
* ✅ Investment suggestions (student/general profile)
* ✅ Sentiment analysis (positive/negative queries)
* ✅ Hybrid approach → Rule-based + AI model (WatsonX Granite)
* ✅ Streamlit UI for an interactive experience

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **IBM WatsonX AI** (Granite model)
* **Hugging Face Transformers** (sentiment analysis)
* **dotenv** (environment variable management)

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit app  
├── requirements.txt      # Dependencies  
├── .env                  # API keys (not uploaded to GitHub)  
├── README.md             # Project documentation  
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/personal-finance-chatbot.git
cd personal-finance-chatbot
```

2. Create a virtual environment & install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your IBM WatsonX credentials:

```
WATSONX_API_KEY=your_api_key
WATSONX_PROJECT_ID=your_project_id
WATSONX_URL=your_url
```

4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🖥️ Usage

* Enter your **salary, expenses, or financial query**.
* The chatbot will provide:

  * 💵 Budget breakdown
  * 🏦 Tax planning advice
  * 📈 Investment suggestions
  * 😊 Sentiment-aware responses

---

## 📊 Example Queries

* *“My salary is 50000, suggest a budget”*
* *“How much tax do I pay if my income is 6 lakhs?”*
* *“I am a student, where should I invest?”*

---

## 🔮 Future Enhancements

* Voice input & speech output
* Connect to real-time financial APIs (stocks, currency rates)
* Personalized recommendations based on spending history

---

## 📜 License

This project is licensed under the **MIT License**.

