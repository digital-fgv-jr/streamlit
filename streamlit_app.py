from matplotlib.pyplot import bar
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("heroes_information.csv")

st.sidebar.header("Title of the side bar")

st.write("Hello person.")

number = st.slider("Select a number", 0, 10, 5, 1)
st.write(f"""
*Oh I see...*

I also like {number} a lot.
""")

st.write("# Very big table here")
st.write(df)

st.bar_chart(df['Weight'])

fig = px.bar(df.sample(10), x="name", y="Height", color="Eye color")
st.plotly_chart(fig)

