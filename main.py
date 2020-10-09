import pandas as pd
from visual import visualize

def rightTime(data):
    l = []
    for i in data:
        if 'P' in i:
            temp = int(i.replace('PM', '').replace(':', ''))
            if 100 <= temp <= 1159:
                temp += 1200
                l.append(temp)
            else:
                l.append(temp)
        else:
            temp = int(i.replace('AM', '').replace(':', ''))
            if 1200 <= temp <= 1259:
                temp -= 1200
                l.append('00' + str(temp))
            elif temp < 1000:
                l.append('0' + str(temp))
            else:
                l.append(temp)
    return pd.Series(l)


def parcer(data):
    data['Time'] = pd.to_datetime(rightTime(data['Time']), format='%H%M').dt.time
    data['Wind Speed'] = data['Wind Speed'].str.replace(r'[a-z]', '').astype(int)
    data['Wind Gust'] = data['Wind Gust'].str.replace(r'[a-z]', '').astype(int)
    data['Pressure'] = data['Pressure'].str.replace(',', '.').astype(float)
    data['day/month'] = data['day/month'] + '.2019'
    data = data.set_index('day/month')
    return data


df = pd.read_csv("DATABASE.csv", sep=';')
df = parcer(df)

need_data = input('Enter the data you want to visualize with comma and space\n').split(', ')

visualize(df, need_data)
