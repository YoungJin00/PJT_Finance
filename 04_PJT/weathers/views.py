from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib.colors import to_rgba

csv_path = 'weathers/data/austin_weather.csv'
plt.switch_backend('Agg')
# Create your views here.
def index(request):
    return render(request, 'base.html')

def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    plt.clf()
    df = pd.read_csv(csv_path, usecols=range(0,4))
    x = pd.to_datetime(df['Date'])
    y1 = df['TempHighF']
    y2 = df['TempAvgF']
    y3 = df['TempLowF']

    plt.plot(x,y1,label="High Temperature")
    plt.plot(x,y2, label="Average Temperature")
    plt.plot(x,y3, label="Low Temperature")

    plt.grid(True)
    plt.xticks(rotation=0)
    plt.legend(loc = 'lower center')

    plt.title("Temperature Variation")
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()


    context = {
        'chart_image' : f'data:/image/png;base64, {image_base64}',
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    plt.clf()
    df = pd.read_csv(csv_path, usecols=range(0,4))
    df['Date'] = pd.to_datetime(df["Date"])
    month_group = df.groupby(df['Date'].dt.to_period('M')).mean()
    x = pd.to_datetime(month_group['Date'])
    y1 = month_group['TempHighF']
    y2 = month_group['TempAvgF']
    y3 = month_group['TempLowF']

    plt.plot(x,y1,label="High Temperature")
    plt.plot(x,y2, label="Average Temperature")
    plt.plot(x,y3, label="Low Temperature")

    plt.title("Temperature Variation")
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')
    plt.legend(bbox_to_anchor=(0.572,0.22)) # 범례박스
    plt.grid() # 뒤에 눈금
    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }  
    return render(request, 'weathers/problem3.html', context)

def problem4(request):
    plt.clf()
    df = pd.read_csv(csv_path)

    # 'Weather' 열의 결측치를 제거하고 ','로 분리하여 다중 값 처리
    df['Events'] = df['Events'].fillna('')  # 결측치를 빈 문자열로 대체
    df['Events'] = df['Events'].str.split(', ')  # ','로 분리하여 리스트로 변환

    # 다중 값들을 하나로 풀어서 새로운 DataFrame 생성
    weather_list = [weather.strip() for sublist in df['Events'].dropna() for weather in sublist]
    weather_df = pd.DataFrame({'Events': weather_list})

    weather_df['Events'] = weather_df['Events'].replace('', 'No events')
    
    weather_df['Events'].value_counts().plot(kind='bar', color='blue')
    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid(True)
    plt.xticks(rotation=0)

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }  
    return render(request, 'weathers/problem4.html', context)


