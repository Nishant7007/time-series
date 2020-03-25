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
def getDashBoardData(request):
	data = json.loads(request.body)["data"]

	chart_type = data["type"]
	item = data["item"]
	mandi = data["mandi"]
	source = data["source"]

	if chart_type == 1:
		past, pred = read_csv(chart_type, item, mandi, source)
		data = {
			"past": past,
			"pred": pred
		}
		return JsonResponse({"data": data})
	else:
		orig, miss = read_csv(chart_type, item, mandi, source)
		data = {
			"orig": orig,
			"miss": miss
		}
		return JsonResponse({"data": data})



def read_csv(chart_type, item, mandi, source):
	base_path = "data/web_data/" + source + "/" + item + "/" + mandi + "/"
	file_path = base_path+"smooth.csv"
	if chart_type == 1:
		file_path_past = base_path+"raw.csv"
		file_path_future = base_path+"predicted.csv"
		print(file_path_past)

		orig, miss = getFileDateAndPrice(file_path_past, days=30)
		past_date_list_orig, past_price_list_orig = orig
		past_date_list_miss, past_price_list_miss = miss


		pred_date_list, pred_price_list = getFileDateAndPrice(file_path_future, pred=True)

		# ((orig), (miss)), (pred_date, pred_price)
		return ((past_date_list_orig, past_price_list_orig), (past_date_list_miss,past_price_list_miss)), (pred_date_list, pred_price_list)




	if chart_type == 2:
		orig, miss = getFileDateAndPrice(file_path, days=365)
		return orig, miss

	if chart_type == 3:
		orig, miss = getFileDateAndPrice(file_path)
		return orig, miss
		


	# if chart_type == 3:
	# 	file_path = base_path+"smooth.csv"
	# 	date_list, price_list = getFileDateAndPrice(file_path)
	# 	# TODO: start from march
	# 	return date_list, price_list
	


def getFileDateAndPrice(file, pred=False, days=-1):
	print("pred", pred)

	if pred:
		date_list = []
		price_list = []

		with open(file) as file:
			for line in file.readlines():
				date, price = line.strip().split(",")
				date_list.append(date)
				price_list.append(price)
		return (date_list, price_list)


	else:
		temp_list = []

		date_list_orig = []
		price_list_orig = []

		date_list_miss = []
		price_list_miss = []

		with open(file) as file:
			for line in file.readlines():
				date, price, is_orig = line.strip().split(",")

				if days == -1:
					date_list_orig.append(date)
					date_list_miss.append(date)
					if bool(float(is_orig)):
						price_list_orig.append(price)
						price_list_miss.append(None)
					else:
						price_list_orig.append(None)
						price_list_miss.append(price)
				else:
					temp_list.append((date, price, is_orig))

		if days > 0:
			temp_list = temp_list[-days:]

			for el in temp_list:
				date, price, is_orig = el
				date_list_orig.append(date)
				date_list_miss.append(date)

				if bool(float(is_orig)):
					price_list_orig.append(price)
					price_list_miss.append(None)
				else:
					price_list_orig.append(None)
					price_list_miss.append(price)





		return (date_list_orig,price_list_orig),  (date_list_miss,price_list_miss)












# 
# 
# archived

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





# type: 1(-30+30)
# type: 2(1 year)
# type: 3(all)
def read_csv1(chart_type, item):
	base_path = "data/"+item+"/"

	if chart_type == 1:
		file_path_past = base_path+"raw.csv"
		file_path_future = base_path+"predicted.csv"

		past_date_list, past_price_list = getFileDateAndPrice(file_path_past)
		past_date_list, past_price_list = past_date_list[-30:], past_price_list[-30:]

		pred_date_list, pred_price_list = getFileDateAndPrice(file_path_future, pred=True)

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

	