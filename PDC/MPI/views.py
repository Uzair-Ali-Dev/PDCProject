from django.http import HttpResponse
from django.shortcuts import render
import os
import time
import random


def home(request):
    args1 = {"operation": "getRegionData"}
    os.system('mpiexec -n 4 python PDCProject-master/script.py "' + str(args1) + '"')
    file = open("PDCProject-master/temp.txt", "r")
    data = file.read().split("\n")
    # print("-------data-------",data)
    file.close()
    Array = []
    chartStr = []
    data = data[0 : len(data) - 1]
    for i in data:
        line = i.split("\t")
       
       
        dit = {
            "zipCode": line[0],
            "zipName": line[1],
            "positiveCount": line[2],
            "totalCount": line[3],
            "positiveRatio": (round((int(line[2]) / int(line[3])) * 100)),
            "vaccinationCount": line[4],
        }

        chartElem = {
            "zipname": (line[1]),
            "positiveCount": int(line[2])*10000,
            "vaccinationCount": int(line[4])*10000,
        }
        chartStr.append(chartElem)
        Array.append(dit)

    dict = {"list": Array, "chartStr": str(chartStr)}

    return render(request, "home.html", dict)


def userDetails(request):
    Array = []
    if request.method == "POST":
        zipcode = request.POST.get("zipcode")
        minAge = request.POST.get("minAge")
        maxAge = request.POST.get("maxAge")
        cnic = request.POST.get("cnic")
        gender = request.POST.get("gender")
        print("Gender", gender)
        if minAge == "" and maxAge == "":
            minAge = 0
            maxAge = 1000
        elif minAge == "" or maxAge == "":
            if minAge == "":
                minAge = 0
            if maxAge == "":
                maxAge = 1000

        args = {
            "operation": "getUserInfo",
            "params": {
                "zipCode": zipcode,
                "minAge": minAge,
                "maxAge": maxAge,
                "cnic": cnic,
                "gender": gender,
            },
        }
        os.system('mpiexec -n 4 python PDCProject-master/script.py "' + str(args) + '"')

        file = open("PDCProject-master/temp.txt", "r")
        data = file.read().split("\n")
        file.close()
        data = data[0 : len(data) - 1]
        counter = 0
        for i in data:
            counter = counter + 1
            line = i.split("\t")
            # print(line[0],line[1])
            if line[6] == "notvaccinated":
                line[6] = "not vaccinated"

            dit = {
                "Sno": counter,
                "Name": line[0],
                "Age": line[1],
                "Cnic": line[2],
                "Gender": line[3],
                "Street": line[4],
                "ZipCode": line[5],
                "Vaccinestatus": line[6],
                "CovidStatus": line[7],
            }
            Array.append(dit)

        dict = {"list": Array}
        return render(request, "userDetails.html", dict)
    return render(request, "userDetails.html")
