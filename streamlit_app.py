from matplotlib.pyplot import bar
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("heroes_information.csv")

# sidebar
st.sidebar.header("Opções")
analise = st.sidebar.radio("Escolha uma análise", ["Objetificação", "Marvel vs DC", "IMC dos Heróis"])

st.subheader("Os dados utilizados advém dessa *database*:")
st.write(df)
st.write("*https://www.kaggle.com/claudiodavi/superhero-set*")

if analise == "Objetificação":
    st.header("Objetificação dos Heróis")
    """
    O Super-man é um homem alto, forte e de olhos azuis. Tal qual é
    o Capitão América. E ainda o Homem Elástico. Diante desse cenário,
    é fácil perceber que isso não se trata de uma coincidência. Principalmente
    no início de seu surgimento, os herois foram criados para representar
    seres sobre-humanos sob todos os aspectos, e a aparência não poderia ser 
    exceção. Afinal, quem respeitaria - e principalmente, quem compraria -
    uma HQ de um Capitão América negro ou obeso em pleno século XX? Baseado nesse
    ponto de vista, essa análise busca evidenciar como a objetificação do corpo
    afetou os nossos herois fantásticos nos últimos anos, em especial às
    personagens femininas.
    """

    st.subheader("Cor dos olhos")
    """
    Sabe-se atualmente que cerca de 90% da população possui olhos castanhos,
    mas essa também é considerada a cor de olhos menos atraente. Por isso,
    vemos nos heróis essa proporção totalmente distorcida.
    """

    # graph olho
    olhos = df.value_counts("Eye color")[:10]
    st.plotly_chart(px.bar(olhos))

    "Nas mulheres, a proporção é ainda mais distópica."
    gender = st.selectbox("Gênero", ["Male", "Female", "-"])
    olhos = df[df["Gender"] == gender].value_counts("Eye color")[:5]
    st.plotly_chart( px.bar(olhos) )
    st.write( olhos )

    # graph cabelo
    st.subheader("Características do cabelo")
    """
    Outra comparação interessante entre gêneros masculino e feminino se dá
    pelas características do cabelo. Por exemplo, há uma quantidade muito maior de mulheres
    com o cabelo loiro e, embora a calvice seja retratada comunmente como uma das consequências
    da aquisição de poderes entre homens, há, por toda a base de dados, apenas duas mulheres
    calvas, sendo uma meio-robô.
    """
    by_gender = st.checkbox("Selecionar por gênero")
    gender2 = st.selectbox("Gênero", ["Male", "Female", "-"], key=1)

    df_calvo = df
    if by_gender:
        df_calvo = df[df["Gender"] == gender2]
    df_calvo = df_calvo.value_counts( "Hair color" )

    st.plotly_chart( px.bar( df_calvo ))
    st.write(df_calvo[:5])

    "Contagem de calvície:"
    df_calvo = df[df["Hair color"] == "No Hair"].value_counts("Gender")

    st.plotly_chart( px.bar( df_calvo ))
# fim da seção 1
#
#
#

# Marvel vs DC
elif analise == "Marvel vs DC":
    st.header("Marvel vs DC")
    """
    A base de dados continha várias publicadoras diferentes, mas todo o resto tinha
    bem pouca informação e não daria pra fazer uma comparação justa. Dados abaixo:
    """
    col1, col2 = st.columns(2)
    col1.write("Publicadoras diferentes:")
    col1.write( pd.unique( df["Publisher"]) )

    col2.write("Quantidade de heróis por publicadora:")
    col2.write( df.value_counts("Publisher"))

    pub = st.selectbox("Selecione sua favorita:", ["Marvel Comics", "DC Comics"], key=2)
    df_base = df[df["Publisher"] == pub]

    "### Quantidade de mocinhos e vilões"
    mocinhos = px.bar( df_base.value_counts("Alignment"))

    st.plotly_chart( mocinhos )

    n_evil = df_base[df_base["Alignment"] == "bad"].shape[0]
    n_good = df_base[df_base["Alignment"] == "good"].shape[0]
    st.metric("Proporção de evil/good:", n_evil/n_good)

    "### Quantidade de raças diferentes:"
    st.write( df_base.value_counts( "Race" ) )
# fim da seção 2
#
#
#
#

# IMC dos Heróis
else:
    hero_name = st.selectbox("Selecione seu herói favorito:", pd.unique( df["name"] ).tolist(), key=3)
    hero = df[df["name"] == hero_name]




    st.header(f"IMC do {hero_name}:")
    coll1, coll2, coll3 = st.columns(3)
    hero_h = hero["Height"].values[0].item() / 100
    hero_w = hero["Weight"].values[0].item()
    imc = hero_w / pow(hero_h, 2)
    delta_from_best = round( ((imc/22) - 1)*100 )

    coll1.metric("Altura", f"{hero_h} m" )
    coll2.metric("Peso", f"{round(hero_w*100)/100} kg")
    coll3.metric("IMC", round(imc*100)/100, f"{delta_from_best}% distante do saudável.")



    