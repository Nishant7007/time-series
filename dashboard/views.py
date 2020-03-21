from django.shortcuts import render
from django.http import HttpResponse
import csv
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
	my_dict = {'insert_me':"Hello I am from views.py!"}
	return render(request,'dashboard/index.html',context=my_dict)


def plot(request):
	return render(request,'dashboard/plot.html')

@csrf_exempt
def getPrice(request):
	data = json.loads(request.body)["data"]
	chart_type = data["type"]
	item = data["item"]
	print(chart_type, item)
	
	date_list, price_list = read_csv(chart_type, item)
	data = {
		"date": date_list,
		"price": price_list
	}
	print("getPrice", chart_type)
	return JsonResponse({"data": data})

def getFileDateAndPrice(file):
	print(file)
	date_list = []
	price_list = []
	with open(file) as file:
		for line in file.readlines():
			date, price = line.strip().split(",")
			date_list.append(date)
			price_list.append(price)

	return date_list, price_list

# type: 1(-30+30)
# type: 2(1 year)
# type: 3(all)
def read_csv(chart_type, item):
	base_path = "data/"+item+"/"

	if chart_type == 1:
		file_path_past = base_path+"raw.csv"
		file_path_future = base_path+"predicted.csv"

		past_date_list, past_price_list = getFileDateAndPrice(file_path_past)
		past_date_list, past_price_list = past_date_list[-30:], past_price_list[-30:]

		pred_date_list, pred_price_list = getFileDateAndPrice(file_path_future)

		return (past_date_list, pred_date_list), (past_price_list, pred_price_list)




	if chart_type == 2:
		file_path = base_path+"raw.csv"
		date_list, price_list = getFileDateAndPrice(file_path)
		return date_list[-365:], price_list[-365:]


	if chart_type == 3:
		file_path = base_path+"smooth.csv"
		date_list, price_list = getFileDateAndPrice(file_path)
		# TODO: start from march
		return date_list, price_list

	