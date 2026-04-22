import streamlit as st
import pandas as pd
from analytics import perform_analytics
from generator import generate_abstract_ref
from recommendations import generate_design_brief, create_rtf_brief

# 1. Настройка страницы (строго в начале)
st.set_page_config(page_title="AI Performance Strategist", layout="wide")

# --- СТИЛИ ДЛЯ АНИМАЦИИ ---
st.markdown("""
    <style>
    @keyframes bounceUp {
        0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
        40% {transform: translateY(-12px);}
        60% {transform: translateY(-6px);}
    }
    .arrow-pointer-up {
        font-size: 18px; font-weight: bold; color: #28a745;
        animation: bounceUp 2s infinite; display: block;
        margin-top: 10px; text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# --- ШАПКА ---
st.title("🚀 AI Performance Creative Strategist")
st.subheader("Интеллектуальный мост между аналитикой и дизайном.")
st.markdown("Система выявляет прибыльные связки в данных и превращает их в ТЗ и референсы.")
st.markdown("---")

# --- SIDEBAR (ЗАГРУЗКА) ---
st.sidebar.header("Data Source")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type="csv")

if not uploaded_file:
    st.sidebar.markdown('<div class="arrow-pointer-up">⬆️ Загрузи файл выше</div>', unsafe_allow_html=True)
    st.info("👈 Начни с загрузки CSV-отчета в боковой панели.")

# --- ОСНОВНОЙ БЛОК ПРИ НАЛИЧИИ ФАЙЛА ---
if uploaded_file:
    # Загрузка и первичный анализ
    df = pd.read_csv(uploaded_file)
    stats_df, summary_text, top_params = perform_analytics(df)

    # Создаем две колонки
    col_left, col_right = st.columns([1, 1], gap="large")

    # ЛЕВАЯ КОЛОНКА: ТЗ
    with col_left:
        st.subheader("🤖 AI Generation: Strategy & Brief")
        with st.spinner("AI пишет ТЗ..."):
            brief = generate_design_brief(top_params)
            st.markdown(brief)

        st.write("---")
        dl_col1, dl_col2 = st.columns(2)
        with dl_col1:
            st.download_button("Download TXT", brief, "brief.txt")
        with dl_col2:
            rtf_data = create_rtf_brief(brief)
            st.download_button("Download RTF", rtf_data, "brief.rtf")

    # ПРАВАЯ КОЛОНКА: ВИЗУАЛ (Которую мы возвращаем)
    with col_right:
        st.subheader("🖼 AI Generation: Visual Reference")
        if st.button("🚀 Generate Visual", use_container_width=True):
            with st.spinner("Генерация изображения через Flux..."):
                img_url = generate_abstract_ref(top_params)
                if "Error" in img_url:
                    st.error(img_url)
                else:
                    st.image(img_url, use_container_width=True)
                    st.success("Референс готов!")