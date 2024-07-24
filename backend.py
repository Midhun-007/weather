import requests


apikey='1b7f7a5ac1717c5bb3e2a75cf1e1de26'
def get_data(place,days,task=None):
    url = "https://api.openweathermap.org/data/2.5" \
          "/forecast?" \
          f"q={place}&appid={apikey}"
    raw_data=requests.get(url)
    data=raw_data.json()
    nr_days=days*8
    filtered_data=data['list'][:nr_days]
    if task=='Temperatures':
        filtered_data=[i['main']['temp'] for i in filtered_data]
    if task=='Day':
        filtered_data=[i['weather'][0]['main'] for i in filtered_data]

    return filtered_data
b=get_data('tokyo',2,'Day')
print(b)

