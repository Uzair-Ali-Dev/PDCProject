from django.http import HttpResponse 
from django.shortcuts import render
import os
import time

def home(request):
    args1 = {"operation": "getRegionData"}
    os.system('mpiexec -n 4 python PDCProject-master/script.py "' + str(args1) + '"')
    file=open("PDCProject-master/temp.txt","r")
    data = file.read().split("\n")
    # print("-------data-------",data)
    file.close()
    Array=[]
    data=data[0:len(data)-1]
    for i in data:
        line=i.split("\t")
        # print(line[0],line[1])
        dit={'zipCode':line[0],'zipName':line[1],'positiveCount':line[2],'totalCount':line[3],'positiveRatio':(round((int(line[2])/int(line[3]))*100))}
        Array.append(dit)
    dict={'list':Array}
    # print("--------------",dict)
    return render(request,"home.html",dict)

def userDetails(request):
    Array=[]
    if request.method == "POST":
        zipcode=request.POST.get("zipcode")
        minAge=request.POST.get("minAge")
        maxAge=request.POST.get("maxAge")
        print(zipcode,minAge,maxAge)
        file = open("PDCProject-master\dummy.txt", "r")
        data = file.read().split("\n")
        file.close()
        for i in data:
            line=i.split("\t")
            print(line[0],line[1])
            dit={'fname':line[0],'lname':line[1]}
            Array.append(dit)
        # print(request.POST.get("zipcode"))
        # list =[{'fname':'abc', 'lname':'cadsad', 'cnic':'321321-21312-231'},{'fname':'abfdsfsdc', 'lname':'cadsafsdfdsd', 'cnic':'34321321-21312-231'}]
        dict={'list':Array}
        return render(request,"userDetails.html", dict)
    return render(request,"userDetails.html")
