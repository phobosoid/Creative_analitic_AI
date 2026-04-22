import streamlit as st
import pandas as pd
from analytics import perform_analytics
from generator import generate_abstract_ref
from recommendations import generate_design_brief, create_rtf_brief

st.set_page_config(page_title="AI Performance Strategist", layout="wide")

st.title("🎨 AI Performance Creative Strategist")
st.markdown("---")

st.sidebar.header("Загрузка данных")
uploaded_file = st.sidebar.file_uploader("Загрузите CSV файл", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    stats_df, summary_text, top_params = perform_analytics(df)

    col_left, col_right = st.columns([1, 1], gap="large")

    with col_left:
        st.subheader("📊 Аналитика и ТЗ")
        st.info(f"**Паттерн:** {summary_text}")

        brief = generate_design_brief(top_params)
        st.markdown(brief)

        st.write("---")
        st.write("📥 **Скачать ТЗ:**")
        dl_col1, dl_col2 = st.columns(2)

        with dl_col1:
            st.download_button("Скачать в TXT", brief, "brief.txt", "text/plain", use_container_width=True)

        with dl_col2:
            rtf_data = create_rtf_brief(brief)
            st.download_button("Скачать в RTF (Word)", rtf_data, "brief.rtf", "application/rtf",
                               use_container_width=True)

    with col_right:
        st.subheader("🖼 Визуальный Референс")
        if st.button("🚀 Сгенерировать референс", use_container_width=True):
            with st.spinner("Генерация через Replicate..."):
                img_url = generate_abstract_ref(top_params)
                if "Error" in img_url:
                    st.error(img_url)
                else:
                    st.image(img_url, use_container_width=True)

else:
    st.warning("👈 Загрузите CSV файл в меню слева.")