import streamlit as st
import requests


st.title('Sistema de recomendação de filmes')
st.sidebar.title("Sobre")
st.sidebar.write("Sistema de recomendação usando TF-IDF e Similaridade")

filme = st.text_input('Digite aqui um filme:', placeholder="Ex: Avengers, Batman...")
if st.button('Recomendar'):
    if filme:
        with st.spinner("Buscando recomendações..."):
            resposta = requests.get(f'http://127.0.0.1:8000/recomendacoes?filme={filme}')
        dados = resposta.json()
        st.success(f"Filme base: {dados['base']}")
        

        if isinstance(dados, dict) and 'error' in dados['recomendacoes']:
            st.error(dados['error'])
        else:
            st.subheader('Filmes recomendados')
            for item in dados['recomendacoes']:
                st.markdown(f"""### 🎬 {item['titulo']}""")
                st.write(f'⭐ Score: {item['score']}')
                st.progress(float(item['score']))
    else:
        st.warning('Digite um filme!')

