import streamlit as st
from json import loads
import pandas as pd

st.markdown('''
# Exibidor de Arquivos

## Suba seu arquivo e vejamos o que acontece

''')

arquivo = st.file_uploader(
    'Suba seu arquivo aqui!',
    type=['jpg', 'png', 'py', 'wav', 'csv', 'json']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'text', 'csv':
            df = pd.read_csv(arquivo)
            st.dataframe(df)            
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        

