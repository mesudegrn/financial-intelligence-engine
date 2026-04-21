import streamlit as st
import google.generativeai as genai
import pandas as pd

# 1. Sayfa ve Tasarım Yapılandırması
st.set_page_config(page_title="GFC AI Analyst", page_icon="📊", layout="centered")
st.title("📊 GFC Financial Analyst")
st.caption("Powered by Gemini 3 Engine | Dataset: MSFT, TSLA, AAPL (2023-2025)")

# 2. Veri Yükleme (Önbellekleme ile optimize edilmiştir)
@st.cache_data
def load_data():
    # Dosya yolunu kendi sisteminize göre güncelleyiniz
    df = pd.read_csv("financial_data.csv", sep=";")
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    context_data = df.to_string(index=False)
except FileNotFoundError:
    st.error("⚠️ financial_data.csv dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")
    st.stop()

# 3. API Yapılandırması
# Güvenlik için API Key'i doğrudan koda yazmak yerine Streamlit secrets veya env kullanılması önerilir.
API_KEY = "AIzaSyDdrNaCOY-eemJfS0TdzA-4yycmfd8gvbc" 
genai.configure(api_key=API_KEY)

@st.cache_resource
def resolve_model_names():
    preferred = [
        "models/gemini-1.5-flash",
        "models/gemini-1.5-pro",
        "models/gemini-2.0-flash",
    ]

    available = [
        m for m in genai.list_models()
        if "generateContent" in getattr(m, "supported_generation_methods", [])
    ]
    names = [m.name for m in available]
    ordered = [name for name in preferred if name in names]
    leftovers = [name for name in names if name not in ordered]
    candidates = ordered + leftovers

    if candidates:
        return candidates

    raise RuntimeError("generateContent destekleyen model bulunamadı.")

# 4. Sohbet Geçmişi (Session State) Yönetimi
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mevcut mesajları ekranda gösterme
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Kullanıcı Girişi ve AI Yanıt Üretimi
if prompt := st.chat_input("Analysis Request (e.g., Which company has the highest revenue?)"):
    
    # Kullanıcı mesajını arayüze ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini 3 API Çağrısı
    with st.chat_message("assistant"):
        prompt_payload = f"""
        Role: Senior Financial Analyst at GFC.
        Task: Analyze the provided 3-year financial data and answer the user query accurately.
        
        DATASET:
        {context_data}
        
        QUERY: {prompt}
        """
        
        try:
            response = None
            last_error = None
            used_model = None

            for model_name in resolve_model_names():
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content(prompt_payload)
                    used_model = model_name
                    break
                except Exception as model_error:
                    err = str(model_error)
                    last_error = model_error
                    # Kota/model hatalarında bir sonraki modele otomatik düş.
                    if ("429" in err) or ("quota" in err.lower()) or ("not found" in err.lower()):
                        continue
                    raise

            if response is None:
                raise last_error if last_error else RuntimeError("Uygun modelle yanıt alınamadı.")

            st.caption(f"Model: {used_model}")
            st.markdown(response.text)
            # AI yanıtını geçmişe ekle
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"⚠️ Service Error: {str(e)}")