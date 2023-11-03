from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd
# Create your views here.

def read_csv(request):
    file_path = 'data/test_data.csv'
    
    df = pd.read_csv(file_path, encoding='cp949')
    data = df.to_dict('records')
    print(df['나이'].mean())
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 


def read_csv_null(request):
    file_path = 'data/test_data_has_null.CSV'
    
    df = pd.read_csv(file_path, encoding='cp949')
    df.fillna('NULL', inplace=True)
    print(df.isna().sum())
    data = df.to_dict('records')
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 

def age_avg(request):
    # file_path = 'data/test_data.csv'
    file_path = 'data/test_data_has_null.CSV'
    
    df = pd.read_csv(file_path, encoding='cp949')
    # average_age = df['나이'].mean()
    average_age = df['나이'].dropna().mean()
    df['diff_age'] = df['나이'].sub(average_age).abs()
    selected_rows = df.nsmallest(10, 'diff_age')
    data = selected_rows.to_dict('records')
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 


def avg_age2(request):
    file_path = 'data/test_data_has_null.CSV'
    df = pd.read_csv(file_path, encoding='cp949')
    avg_age = df['나이'][df['나이'] != 'NULL'].mean()
    df['평균나이와의 차이'] = abs(df['나이'] - avg_age)
    new_df = df.sort_values(by=['평균나이와의 차이'])[0:10]
    new_df.drop(['평균나이와의 차이'], axis=1, inplace=True)
    data = new_df.to_dict(orient='records')
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 