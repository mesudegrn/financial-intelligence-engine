# 📊 Financial Intelligence Engine: From Rule-Based Logic to RAG-Augmented AI

## 📌 Project Overview & Strategic Context
This project was developed within the framework of the **BCG (Boston Consulting Group) Strategic Financial Analysis Job Simulation**. It aims to replicate the high-stakes analytical rigor required in management consulting by transforming raw financial data into actionable strategic insights.

The repository showcases a dual-engine architecture designed to process 10-K data (2023-2025) for **Apple (AAPL), Microsoft (MSFT), and Tesla (TSLA)**, evolving from a deterministic engineering approach to an advanced AI-driven advisory interface.

## ⚙️ The Dual-Engine Architecture

To meet the "zero-error" standards of top-tier consulting, the system employs a hybrid methodology:

### 🔹 Phase 1: The Deterministic Sentinel (Consulting Core)
* **Objective:** Ensure 100% data integrity for financial auditing.
* **Tech:** Python, Pandas.
* **Method:** Automated computation of key performance indicators (KPIs) like YoY Growth and Asset Turnover. By using rule-based logic, this engine eliminates **AI Hallucinations**, providing a "Single Source of Truth" for quantitative reporting.

### 🔹 Phase 2: The Strategic Oracle (Gemini 3 & RAG)
* **Objective:** Deliver executive-level qualitative reasoning.
* **Tech:** Google Gemini 3 (State-of-the-art Engine), Google GenAI SDK.
* **Architecture:** **Retrieval-Augmented Generation (RAG)** framework.
* **Method:** This layer acts as a **Senior Consultant**. It doesn't just pull numbers; it synthesizes the data to answer complex "Why?" questions, such as analyzing the impact of margin compression on long-term valuation.

## 🛠️ Technology Stack
* **Analytical Engine:** Python 3.12+, Pandas, NumPy
* **Generative AI:** Google GenAI SDK (Gemini 3 Flash/Pro)
* **NLP Architecture:** Retrieval-Augmented Generation (RAG)
* **Delivery Interface:** Streamlit (Configured with a professional, dark-themed UI)

## 🚀 Key Strategic Insights Delivered
* 📈 **Automated KPI Dashboard:** Instant visualization of 3-year revenue trajectories and net income margins.
* 🔍 **Comparative Intelligence:** Cross-company benchmarking to identify market leaders and operational laggards.
* 🧠 **LLM-Powered Reasoning:** Professional, consultant-grade analysis generated through high-fidelity context injection.

## 🚀 How to Run Locally

**1. Clone the repository**
bash
git clone [https://github.com/yourusername/financial-intelligence-engine.git](https://github.com/mesudegrn/financial-intelligence-engine.git)
cd financial-intelligence-engine

**2. Install required libraries**

Bash
pip install -r requirements.txt

**3. Add your API Key**
You need a free Google Gemini API key to run the AI engine. Set it as an environment variable in your terminal:
For Windows (Command Prompt):

DOS
set GEMINI_API_KEY="your_api_key_here"
For Mac/Linux:

Bash
export GEMINI_API_KEY="your_api_key_here"


**4. Start the Application**

Bash
streamlit run app.py
(This will automatically open the AI Chatbot interface in your web browser).
