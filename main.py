import streamlit as st
import plotly.express as px
from backend import get_data
st.title('Weather forecast app')
place=st.text_input('PLace:')
days=st.slider('No of days to forcast',min_value=1,max_value=5,help='Select the no of days to forcast')
task=st.selectbox('What to You want to forecast',('Temperatures','Day'))
st.subheader(f"{task} forecast of {days} days of {place}")

try:
    if place!=None:
        filtered_data = get_data(place, days, task=None)
        if task == 'Temperatures':
            temperatures = [int(i['main']['temp'])/10 for i in filtered_data]
            print(temperatures)
            print(days)
            dates=[i['dt_txt'] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature'})
            st.plotly_chart(figure)
        if task == 'Day':
            sky = [i['weather'][0]['main'] for i in filtered_data]
            images={'Clear':'images/rain.png','Snow':'images/snow.png'
                    ,'Clouds':'images/cloud.png','Rain':'images/rain.png'}
            image_paths=[images[condition] for condition in sky]
            col1,col2=st.columns(2)
            dates = [i['dt_txt'] for i in filtered_data]
            print(dates)
            with col1:
                for i in dates:
                    st.write(i)
                    st.write('')
                    st.write('')
                    st.write('')
            with col2:
                for j in image_paths:
                    st.image(j,width=120)
except KeyError:
    print('HI')

