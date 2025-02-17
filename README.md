# 🚀 Python Code Reviewer

##[Python Code Reviewer APP](https://python-code-ai-reviewer-k4kzxnmvdzxxx8tise5et5.streamlit.app)

## 📌 Project Overview
This is a **Streamlit web application** that utilizes **Google Gemini AI** to review Python code. It analyzes the given Python script, detects errors, suggests optimizations, and provides a final rating based on best coding practices.


## 🎯 Features
- **Code Analysis**: Explains the functionality of the provided Python code.
- **Error Detection**: Identifies syntax, logical, and runtime issues.
- **Performance Optimization**: Suggests ways to improve code efficiency.
- **Best Practices**: Recommends improvements for readability, maintainability, and security.

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit  
- **Backend AI Model**: Google Gemini AI (Gemini 2.0 Pro)  
- **Deployment**: Streamlit Cloud  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/python-code-reviewer.git
cd python-code-reviewer
```

### 2️⃣ Install Dependencies
Ensure you have Python installed (recommended **Python 3.8+**). Then, install the required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key
Create a **.env** file in the project root and add your **Google Gemini API key**:
```bash
GENAI_API_KEY=your_google_gemini_api_key
```
Alternatively, replace the API key directly in the `app.py` file (not recommended for security reasons).

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```
This will launch the application in your browser at **http://localhost:8501**

---

## ☁️ Deployment on Streamlit Cloud

### 1️⃣ Create a GitHub Repository
Push your project to a GitHub repository.

### 2️⃣ Deploy on Streamlit Cloud
1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Click **New App**
3. Connect your GitHub repository
4. Select the **branch** and **app.py** as the main script
5. Click **Deploy**

### 3️⃣ Configure Environment Variables
- In Streamlit Cloud, navigate to **App Settings > Secrets**
- Add your API key as:
  ```bash
  GENAI_API_KEY=your_google_gemini_api_key
  ```

Your Streamlit app is now live! 🎉
