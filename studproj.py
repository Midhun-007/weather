import streamlit as st
import pandas as pd
import plotly.express as px

st.title('IN SEARCH OF HAPPINESS')
X = st.selectbox('Select x axis', ('happiness', 'gdp', 'generosity'))
Y = st.selectbox('select y axis', ('happiness', 'gdp', 'generosity'))
df = pd.read_csv('happy.csv')
x1 = df[X]
y1 = df[Y]
figure = px.scatter(x=x1, y=y1,labels={'x':X,'y':Y})
st.plotly_chart(figure)
