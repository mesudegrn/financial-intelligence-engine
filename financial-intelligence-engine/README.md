# 📊 Financial Intelligence Engine: Rule-Based to Generative AI

## 📌 Project Overview
This repository showcases a comprehensive financial data analysis pipeline, evolving from a deterministic, rule-based logic system into a dynamic, AI-powered analytical interface. The project utilizes official financial data (2023-2025) from industry leaders: **Apple (AAPL), Microsoft (MSFT), and Tesla (TSLA)**.

The core objective is to demonstrate the optimization of financial data processing and the deployment of a dual-engine chatbot architecture for instant data retrieval and strategic reasoning.

## ⚙️ The Dual-Engine Architecture

This project is built upon two distinct phases, highlighting the progression from strict data engineering to advanced Natural Language Processing (NLP).

### Phase 1: The Deterministic Engine (Rule-Based Logic)
Located in `financial_analysis.ipynb`.
Before introducing AI, it is critical to ensure data integrity. This phase involves:
* **Data Engineering:** Cleaning and structuring raw SEC 10-K data using `pandas`.
* **Metric Calculation:** Automated computation of YoY Revenue Growth, Net Income Growth, and Asset Turnover.
* **Manual Chatbot Prototype:** A custom-built, `if-else` driven command-line interface. This engine guarantees 100% accuracy with zero risk of AI hallucination by utilizing explicit keyword extraction and mapping.

### Phase 2: The Generative AI Engine (Gemini 3 Integration)
Located in `app.py`.
To move beyond static queries, the project integrates a Retrieval-Augmented Generation (RAG) approach using the **Google GenAI SDK**.
* **LLM Integration:** Powered by the state-of-the-art `gemini-3-flash-preview` model.
* **Strategic Reasoning:** The model does not just retrieve numbers; it analyzes trends, compares cross-company metrics, and explains the *why* behind the financial shifts.
* **Modern UI Deployment:** The AI engine is wrapped in a sleek, Dark Mode-supported web interface built with `Streamlit`, providing a seamless user experience.

## 🛠️ Technology Stack
* **Language:** Python 3.12+
* **Data Processing:** Pandas
* **Generative AI:** Google GenAI SDK (Gemini 3)
* **Web Interface:** Streamlit

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
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