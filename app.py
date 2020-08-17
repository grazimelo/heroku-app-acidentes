import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import folium 
from streamlit_folium import folium_static
from folium.plugins import HeatMap
from folium.plugins import HeatMapWithTime
from folium import plugins




def main():
    st.title("Análise sobre os Acidentes nas Rodovias Federais do Brasil no Ano de 2019.")
    st.image('psicologia-do-transito.jpg')
    df = pd.read_csv('acidentes.csv', sep=';')
    st.markdown('O intuito de analisar este dataset foi procurar responder algumas perguntas, sobre os acidentes das Rodovias Federais do Brasil no ano de 2019.')
    slider = st.slider('Primeira visualizacao geral dos dados.')
    st.dataframe(df.head(slider))

    #Selecionando estado das vitimas 
    st.markdown('Dados sobre as vitímas')
    select_method = st.radio('Escolha uma opção abaixo para o estado físico das vítimas: ', ('Ilesos', 'Feridos leves', 'Feridos graves', 'Mortos', 'Porcentagem de todas as vítimas registradas.'))
    if select_method == 'Ilesos':
        st.markdown('Foram contabilizados em 2019 cerca de :'  + str(df['ilesos'].sum()) + ' vitímas de acidentes sem ferimentos.')
    if select_method == 'Feridos leves':
        st.markdown('Foram contabilizados em 2019 cerca de :'  + str(df['feridos_leves'].sum()) + ' vitímas de acidentes com ferimentos leves.')
    if select_method == 'Feridos graves':
        st.markdown('Foram contabilizados em 2019 cerca de :'  + str(df['feridos_graves'].sum()) + ' vitímas de acidentes com ferimentos graves.')
    if select_method == 'Mortos':
        st.markdown('Foram contabilizados em 2019 cerca de :'  + str(df['mortos'].sum()) + ' vitímas de acidentes fatáis.')
    if select_method == 'Porcentagem de todas as vítimas registradas.':
        st.markdown('O total em %: ' + str(round(df[['ilesos','feridos_leves','feridos_graves','mortos']].sum()/len(df[['ilesos','feridos_leves','feridos_graves','mortos']]) * 100,1)))


    #agrupando estados com br e estados das vitimas

    st.title('Análises individuais por estados.')
    df_estado = df.groupby(['uf'])['ilesos','feridos_leves','feridos_graves','mortos'].sum().reset_index()
    estado = st.selectbox('Escolha um estado: ', df_estado['uf'])


    if estado == 'AC': 
        st.write(df_estado[df_estado['uf'] == 'AC'])
        st.bar_chart(df_estado[df_estado['uf'] == 'AC'].T, width=200, height = 300)
    if estado == 'AL': 
        st.write(df_estado[df_estado['uf'] == 'AL'])
        st.bar_chart(df_estado[df_estado['uf'] == 'AL'].T, width=200, height = 300)
    if estado == 'AP': 
        st.write(df_estado[df_estado['uf'] == 'AP'])
        st.bar_chart(df_estado[df_estado['uf'] == 'AP'].T, width=200, height = 300)
    if estado == 'AM': 
        st.write(df_estado[df_estado['uf'] == 'AM'])
        st.bar_chart(df_estado[df_estado['uf'] == 'AM'].T, width=200, height = 300)
    if estado == 'RR': 
        st.write(df_estado[df_estado['uf'] == 'RR'])
        st.bar_chart(df_estado[df_estado['uf'] == 'RR'].T, width=200, height = 300)
    if estado == 'TO': 
        st.write(df_estado[df_estado['uf'] == 'TO'])
        st.bar_chart(df_estado[df_estado['uf'] == 'TO'].T, width=200, height = 300)
    if estado == 'RO': 
        st.write(df_estado[df_estado['uf'] == 'RO'])
        st.bar_chart(df_estado[df_estado['uf'] == 'RO'].T, width=200, height = 300)
    if estado == 'DF': 
        st.write(df_estado[df_estado['uf'] == 'DF'])
        st.bar_chart(df_estado[df_estado['uf'] == 'DF'].T, width=200, height = 300)
    if estado == 'MS': 
        st.write(df_estado[df_estado['uf'] == 'MS'])
        st.bar_chart(df_estado[df_estado['uf'] == 'MS'].T, width=200, height = 300)
    if estado == 'SC': 
        st.write(df_estado[df_estado['uf'] == 'SC'])
        st.bar_chart(df_estado[df_estado['uf'] == 'SC'].T, width=200, height = 300)
    if estado == 'PB': 
        st.write(df_estado[df_estado['uf'] == 'PB'])
        st.bar_chart(df_estado[df_estado['uf'] == 'PB'].T, width=200, height = 300)
    if estado == 'PI': 
        st.write(df_estado[df_estado['uf'] == 'PI'])
        st.bar_chart(df_estado[df_estado['uf'] == 'PI'].T, width=200, height = 300)
    if estado == 'ES': 
        st.write(df_estado[df_estado['uf'] == 'ES'])
        st.bar_chart(df_estado[df_estado['uf'] == 'ES'].T, width=200, height = 300)
    if estado == 'MA': 
        st.write(df_estado[df_estado['uf'] == 'MA'])
        st.bar_chart(df_estado[df_estado['uf'] == 'MA'].T, width=200, height = 300)
    if estado == 'PR': 
        st.write(df_estado[df_estado['uf'] == 'PR'])
        st.bar_chart(df_estado[df_estado['uf'] == 'PR'].T, width=200, height = 300)
    if estado == 'GO': 
        st.write(df_estado[df_estado['uf'] == 'GO'])
        st.bar_chart(df_estado[df_estado['uf'] == 'GO'].T, width=200, height = 300)
    if estado == 'RN': 
        st.write(df_estado[df_estado['uf'] == 'RN'])
        st.bar_chart(df_estado[df_estado['uf'] == 'RN'].T, width=200, height = 300)
    if estado == 'SP': 
        st.write(df_estado[df_estado['uf'] == 'SP'])
        st.bar_chart(df_estado[df_estado['uf'] == 'SP'].T, width=200, height = 300)
    if estado == 'RJ': 
        st.write(df_estado[df_estado['uf'] == 'RJ'])
        st.bar_chart(df_estado[df_estado['uf'] == 'RJ'].T, width=200, height = 300)
    if estado == 'PE': 
        st.write(df_estado[df_estado['uf'] == 'PE'])
        st.bar_chart(df_estado[df_estado['uf'] == 'PE'].T, width=200, height = 300)
    if estado == 'MG': 
        st.write(df_estado[df_estado['uf'] == 'MG'])
        st.bar_chart(df_estado[df_estado['uf'] == 'MG'].T, width=200, height = 300)
    if estado == 'SE': 
        st.write(df_estado[df_estado['uf'] == 'SE'])
        st.bar_chart(df_estado[df_estado['uf'] == 'SE'].T, width=200, height = 300)
    if estado == 'RS': 
        st.write(df_estado[df_estado['uf'] == 'RS'])
        st.bar_chart(df_estado[df_estado['uf'] == 'RS'].T, width=200, height = 300)
    if estado == 'BA': 
        st.write(df_estado[df_estado['uf'] == 'BA'])
        st.bar_chart(df_estado[df_estado['uf'] == 'BA'].T, width=200, height = 300)
    if estado == 'PA': 
        st.write(df_estado[df_estado['uf'] == 'PA'])
        st.bar_chart(df_estado[df_estado['uf'] == 'PA'].T, width=200, height = 300)
    if estado == 'MT': 
        st.write(df_estado[df_estado['uf'] == 'MT'])
        st.bar_chart(df_estado[df_estado['uf'] == 'MT'].T, width=200, height = 300)
    if estado == 'CE': 
        st.write(df_estado[df_estado['uf'] == 'CE'])
        st.bar_chart(df_estado[df_estado['uf'] == 'CE'].T, width=200, height = 300)

    st.title('Br com maiores índices de acidentes.')
    df['br'].value_counts().head(10).sort_values(ascending= True).plot.barh()
    st.pyplot()
    st.markdown('A Br em que há mais acidentes é a Br 101,116,381, respectivamente.')


    st.title('Estados com maiores índices de acidentes')
    #Estados onde há mais acidentes
    fig = plt.figure(figsize=(12,10))
    fig = df['uf'].value_counts().head(10).sort_values(ascending= True).plot.barh()
    fig.set_title("Estados com maiores índices de acidentes.")
    fig.set_xlabel('Quantidade.')
    fig.set_ylabel('Estados')
    st.pyplot()
    st.markdown('O estado brasileiro que mais possui acidentes é Minas Gerais, seguido de Santa Catarina e Paraná.')


    st.title('Dia da semana que mais ocorrem acidentes.')
    fig = plt.figure(figsize=(12,8))
    fig = df['dia_semana'].value_counts().sort_values(ascending= True).plot.barh()
    fig.set_title("Dia em que há mais acidentes")
    fig.set_xlabel('Quantidade')
    fig.set_ylabel('Dia da semana')
    st.pyplot()
    st.markdown('Os acidentes ocorrem mais nos fins de semana, geralmente.')


    st.title('Faixa etária das vítimas envolvidas.')
    plt.figure(figsize=(12,8))
    sns.countplot(x='idade',data=df,hue='estado_fisico')
    plt.xlabel('Tipo de pessoa. ',size=8)
    plt.ylabel('Número de vítimas.')
    st.pyplot()
    st.markdown('A maior parte das vítimas envolvidas dos acidentes são adultos.')


    st.title('Maiores causas de acidentes.')
    fig = plt.figure(figsize=(12,10))
    fig = df['causa_acidente'].value_counts().head(15).sort_values(ascending= True).plot.barh()
    fig.set_title("Maiores causas de acidentes.")
    fig.set_xlabel('Quantidade.')
    fig.set_ylabel('Causas')
    st.pyplot()
    st.markdown('O top 5 das maiores causas de acidentes no ano de 2019 foi devido a falta de atenção à condução, seguido de desobediência as normas de trânsito pelo condutor, velocidade incompatível, ingestão de álcool e não aderir a distância miníma de segurança.')


    st.title('Relação entre o tipo do acidente e vítimas.')
    tipo_de_acidente= df.groupby('tipo_acidente')[['mortos']].count().sort_values(by='mortos',ascending= False).head(20)
    tipo_de_acidente.reset_index(inplace=True)
    plt.figure(figsize=(30,10))
    sns.pointplot(x='tipo_acidente', y='mortos',data=tipo_de_acidente)
    plt.xticks(rotation=50)
    plt.title('Relação entre tipo de acidentes e vítimas.')
    st.pyplot()
    st.markdown('Os principais tipo de acidentes são: Colisão traseira, seguido por colisão transversal, saída de leito carroçável e colisão frontal.')


    st.title('Mapa de calor representando as Br e os acidentes.')

    coordenadas=[]

    for lat,lng in zip(df.latitude.values[:162273],df.longitude.values[:162273]):
        coordenadas.append([lat,lng])
    mapa = folium.Map(location=[-15.788497,-47.879873],zoom_start=6,tiles='Stamen Terrain')
    mapa.add_child(plugins.HeatMap(coordenadas))   
    folium_static(mapa)
    st.markdown('Mapa de calor representando os locais em que há uma maior concentração de acidentes(vermelho).')


    st.title('Mapa interativo dos Acidentes de 2019 de janeiro até dezembro.')
    #Mapa interativo dos Acidentes de 2019 de 1 até 365.
    df['acidente'] = 1
    df = df.groupby(['data_inversa','latitude','longitude']).agg({'acidente':'sum'}).reset_index()
    base_map = folium.Map(location = [-15, -47],control_scale=True, zoom_start=4.5)
    df = df.sort_values(by='data_inversa')
    df_date_lat_lon_list = []
    for hour in df.data_inversa.sort_values().unique():
        df_date_lat_lon_list.append(df.loc[df.data_inversa == hour, ['latitude', 'longitude', 'acidente']].values.tolist())
    #Plotando gráfico. 
    HeatMapWithTime(df_date_lat_lon_list, radius=5, gradient={0.1: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'}, min_opacity=0.5, max_opacity=0.8, use_local_extrema=True).add_to(base_map)
    folium_static(base_map)
    st.markdown('Mapa interativo representando todos os acidentes registrados ao longo do ano de 2019.')
    
if __name__ == '__main__':
      main()