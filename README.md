# 🤖 GenAI Chatbot (Ollama + LangChain)

A simple and powerful **GenAI chatbot** built using **LangChain, Ollama, and Streamlit** that runs completely **locally** without any external API costs.

---

## 🚀 Features

* 💬 Interactive chatbot UI using Streamlit
* 🧠 Powered by local LLM (Ollama - Gemma 2B)
* ⚡ Fast and lightweight
* 🔒 Runs offline (no API key required)
* 🧩 Beginner-friendly project

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **LangChain Core**
* **Ollama (Local LLM)**
* **Gemma:2B Model**

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/genai-chatbot-ollama.git
cd genai-chatbot-ollama
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Ollama

### Install Ollama:

👉 https://ollama.com/download

---

### Pull model:

```bash
ollama pull gemma:2b
```

---

### Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📸 Demo

Type your question in the input box and the chatbot will respond instantly.

Example:

```
You: What is AI?
Bot: Artificial Intelligence is...
```

---

## 📁 Project Structure

```
genai-chatbot-ollama/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🎯 Learning Outcomes

* Understanding of **LLMs and GenAI basics**
* Working with **LangChain pipelines**
* Building UI with **Streamlit**
* Running models locally using **Ollama**

---

## 🚀 Future Improvements

* 🧠 Add chat memory
* 📄 PDF question-answering chatbot
* 🎨 ChatGPT-like UI
* 🔊 Voice input/output


