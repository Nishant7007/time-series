from django.shortcuts import render
from django.http import HttpResponse
import csv
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
import pandas as pd
from datetime import datetime, timedelta
import calendar
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

data_path = "data/webpage"

def base(request):
    return render(request, 'home/base.html')

# data_type = Price/ Retail/ Arrival
def read_original_data(aggregate=False, commodity_name="Onion", data_type="Price", mandi_name="Lasalgaon", state_name="Maharashtra", from_date="2019-10-1", to_date="2020-9-30"):
    # from_date = datetime.strptime(from_date, "%Y-%m-%d").date()    
    # to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
    from_date = pd.to_datetime(from_date, format="%Y-%m-%d") 
    to_date = pd.to_datetime(to_date, format="%Y-%m-%d")

    file_path = ""
    if not aggregate:
        file_path = f"{data_path}/{commodity_name}/Original/{state_name}_{mandi_name}_{data_type}.csv"
        df = pd.read_csv(file_path)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d') 
        df = df[(df["DATE"] >= from_date) & (df["DATE"] <= to_date)]
        # do smooothing
        df["DATE"] = df["DATE"].astype(str)
        date = df["DATE"].to_list()
        value = df["ARRIVAL" if data_type=="Arrival" else "PRICE"].to_list()
        return (date, value)

    if aggregate:
        file_path = f"{data_path}/{commodity_name}/Original/Avg_Std_{data_type}.csv"
        df = pd.read_csv(file_path)
        df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d') 
        df = df[(df["DATE"] >= from_date) & (df["DATE"] <= to_date)]
        df["DATE"] = df["DATE"].astype(str)
        date = df["DATE"].to_list()
        AVG = df["AVG"].to_list()
        STD = df["STD"].to_list()

        return (date, AVG, STD)

@csrf_exempt
def get_mandi_data_1_year(request):
    data = json.loads(request.body)["data"]
    commodity_name = data["commodity_name"]
    mandi_name = data["mandi_name"]
    state_name = data["state_name"]


    date, mandi_price = read_original_data(aggregate=False, commodity_name=commodity_name, data_type="Price", mandi_name=mandi_name, state_name=state_name, from_date="2019-8-1", to_date="2020-8-31")
    date, retail_price = read_original_data(aggregate=False, commodity_name=commodity_name, data_type="Retail", mandi_name=mandi_name, state_name=state_name, from_date="2019-8-1", to_date="2020-8-31")
    date, arrival = read_original_data(aggregate=False, commodity_name=commodity_name, data_type="Arrival", mandi_name=mandi_name, state_name=state_name, from_date="2019-8-1", to_date="2020-8-31")

    date, mandi_avg, mandi_std = read_original_data(aggregate=True, commodity_name=commodity_name, data_type="Price", mandi_name=mandi_name, state_name=state_name, from_date="2019-8-1", to_date="2020-8-31")
    date, retail_avg, retail_std = read_original_data(aggregate=True, commodity_name=commodity_name, data_type="Retail", mandi_name=mandi_name, state_name=state_name, from_date="2019-8-1", to_date="2020-8-31")
    date, arrival_avg, arrival_std = read_original_data(aggregate=True, commodity_name=commodity_name, data_type="Arrival", mandi_name=mandi_name, state_name=state_name, from_date="2019-8-1", to_date="2020-8-31")


    response = {
        "date":date,

        "mandi_price": mandi_price,
        "retail_price":retail_price,
        "arrival":arrival,

        "mandi_avg": mandi_avg,
        "retail_avg": retail_avg,
        "arrival_avg": arrival_avg,

        "mandi_std": mandi_std,
        "retail_std": retail_std,
        "arrival_std": arrival_std

    }

    return JsonResponse({"data": response})


        