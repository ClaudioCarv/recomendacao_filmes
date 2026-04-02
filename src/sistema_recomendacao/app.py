import streamlit as st
import requests


st.title('Sistema de recomendação de filmes')
st.sidebar.title("Sobre")
st.sidebar.write("Sistema de recomendação usando TF-IDF e Similaridade")
API_URL = "https://recomendacao-filmes-api.onrender.com"
filme = st.text_input('Digite aqui um filme:', placeholder="Ex: Avengers, Batman...")

if st.button('Recomendar'):
    if filme:
        with st.spinner("Buscando recomendações..."):
            try:
                resposta = requests.get(f'https://recomendacao-filmes-api.onrender.com/recomendacoes?filme={filme}')
                dados = resposta.json()
            except  requests.exceptions.RequestException:
                st.error('Erro ao conectar com a API')
                st.stop()

        st.success(f"Filme base: {dados['base']}")
        

        if isinstance(dados, dict) and 'error' in dados['recomendacoes']:
            st.error(dados['error'])
            st.info("💡 Dica: tente nomes em inglês ou mais curtos")
        else:
            st.subheader('Filmes recomendados')
            for item in dados['recomendacoes']:
                st.markdown(f"""### 🎬 {item['titulo']}""")
                st.write(f'⭐ Score: {item['score']}')
                st.progress(float(item['score']))
    else:
        st.warning('Digite um filme!')

