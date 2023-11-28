
import datetime
import json
import requests
import pandas as pd
 
OIKO_KEY = '1ac249c703ba490dbda4024760358300'
URL = 'https://api.oikolab.com/weather'

def get_temperature(start_date, end_date, city):
 
    resp = requests.get(URL,
        params = {
            'param': ['temperature'],
            'start': start_date,
            'location': city,
            'end': end_date,
            'api-key': OIKO_KEY,
            'freq': 'D'
            }
    )
    weather_data = json.loads(resp.json()['data'])
    df = pd.DataFrame(index=pd.to_datetime(weather_data['index'],unit='s'),
                    data=weather_data['data'],
                    columns=weather_data['columns'])
 
    # print(df.iloc[:,4])
    return df.iloc[:,4]
 
def print_comparison(start_date, end_date, city1, city2):
 
    city1_data = get_temperature(start_date, end_date, city1)
    city1_temp_variance = city1_data.var()
 
    city2_data = get_temperature(start_date, end_date, city2)
    city2_temp_variance = city2_data.var()
 
    if city1_temp_variance < city2_temp_variance:
        print(f'We choose {city1} because of less temperature variance')
    else:
        print(f'We choose {city2} because of less temperature variance')
 
 
 
 
 
 
city1 = input()
city2 = input()
start_date = input()
start_date = list(map(int, start_date.split('-')))
obj1 = datetime.datetime(start_date[0], start_date[1], start_date[2],0,0)
 
obj2 = obj1 + datetime.timedelta(days=7)
 
start_date = obj1.strftime('%Y-%m-%d')
end_date = obj2.strftime('%Y-%m-%d')
 
print_comparison(start_date, end_date, city1, city2)