# 🌍 Classificador Binário de Poluição em Rios com Deep Learning

Este projeto é uma aplicação baseada em **redes neurais convolucionais (CNN)** que classifica imagens de rios como **poluídos ou não poluídos**.

A interface foi construída com [Streamlit](https://streamlit.io/) e permite que qualquer usuário envie imagens e visualize a predição do modelo de forma intuitiva.

---

## 🧪 Demonstração online

Você pode acessar e testar o modelo diretamente [clicando aqui](https://seu-link-no-streamlit.streamlit.app).

---

## 📸 Como funciona

1. O usuário envia uma ou mais imagens de rios.
2. As imagens são processadas e redimensionadas para o modelo.
3. O modelo retorna a probabilidade de poluição (0% a 100%).
4. A interface exibe resultados individuais e uma média geral.

---

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/classificador-poluicao-rios.git
cd classificador-poluicao-rios

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
streamlit run app.py
```

---

## 📂 Dataset

As imagens utilizadas no treinamento do modelo foram obtidas a partir de imagens públicas com creative commons e dos dataset [** debris Dataset **](https://universe.roboflow.com/debris-qtddn/debris-ikfey) e [** marine debris Dataset **](https://universe.roboflow.com/marine-debris/marine-debris-i2ge3)
Essas imagens foram utilizadas apenas para **fins educacionais e de pesquisa**, respeitando os direitos dos autores originais.


---  

## 🧪 Tecnologias utilizadas
- Python
- TensorFlow / Keras
- Streamlit
- NumPy / PIL

## 👩‍💻 Autoria
Desenvolvido por Jullia Fernandes

CEFET-MG – Campus Divinópolis

Projeto de pesquisa / artigo científico