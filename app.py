import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model

# ========== ESTILO CSS ==========
st.markdown("""
    <style>
    .main {
        background-color: #f7fcff;
    }
    h1 {
        color: #007acc;
    }
    .stButton>button {
        background-color: #007acc;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
""", unsafe_allow_html=True)

# ========== CARREGAMENTO DO MODELO ==========
model = load_model("melhor_modelo2.h5", compile=False)

# ========== TÍTULO E DESCRIÇÃO ==========
st.markdown("# 🌍 Classificação Binário de Rios por Imagem")
st.markdown("🔍 **Descubra se um rio está poluído com a ajuda de inteligência artificial!**")
st.markdown("Envie imagens e veja o modelo analisar automaticamente a **probabilidade de poluição** com base visual.")

# ========== INFO EXPANDIDA ==========
with st.expander("ℹ️ Sobre o modelo"):
    st.write("""
    Este modelo foi treinado com imagens de rios poluídos e não poluídos usando uma Rede Neural Convolucional (CNN).
    O valor de saída representa a **probabilidade de poluição**, variando de 0% (sem poluição) a 100% (muito poluído).
    """)

# ========== UPLOAD DE IMAGENS ==========
uploaded_files = st.file_uploader("📸 Envie uma ou mais imagens do rio", 
                                   type=["jpg", "jpeg", "png"], 
                                   accept_multiple_files=True)

# ========== CLASSIFICAÇÃO ==========
if uploaded_files:
    if st.button("🔎 Verificar"):
        total_poluido = 0
        probs = []

        st.markdown("---")
        st.subheader("📋 Resultados individuais")

        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file).convert("RGB")
            img_resized = image.resize((224, 224))
            img_array = np.array(img_resized) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            prob = prediction[0][0]
            probs.append(prob)

            # Layout em colunas
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(image, width=200, caption=uploaded_file.name)
            with col2:
                st.write(f"📊 **Probabilidade de poluição:** `{prob * 100:.2f}%`")
                if prob > 0.5:
                    st.error("🚨 O rio está **POLUÍDO**")
                    total_poluido += 1
                else:
                    st.success("✅ O rio **NÃO está poluído**")

            st.markdown("---")

        # Resultado final
        st.subheader("📈 Resumo geral:")
        st.write(f"🖼️ Total de imagens analisadas: **{len(uploaded_files)}**")
        st.write(f"🌊 Imagens classificadas como poluídas: **{total_poluido}**")
        st.write(f"📉 Média de poluição estimada: **{np.mean(probs)*100:.2f}%**")

st.markdown("---")
st.markdown("© 2025 Jullia Fernandes | CEFET-MG – Campus Divinópolis")

with st.expander("📄 Licença e créditos"):
    st.markdown("""
    - Este projeto está licenciado sob a **MIT License**.
    - As imagens utilizadas pertencem aos autores originais do dataset e foram usadas apenas para fins acadêmicos.
    - Desenvolvido como parte de um projeto acadêmico em Ciência de Dados.
    """)