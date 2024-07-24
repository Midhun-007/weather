import streamlit as st
import plotly.express as px
st.title('Weather forecast app')
place=st.text_input('PLace:')
days=st.slider('No of days to forcast',min_value=1,max_value=5,help='Select the no of days to forcast')
task=st.selectbox('What to You want to forecast',('Temperatures','Day'))
st.subheader(f"{task} forecast of {days} days of {place}")
figure=px.line(x=[10,12,13],y=[10,9,8],labels={'x':'Date','y':'Temperature'})
st.plotly_chart(figure)