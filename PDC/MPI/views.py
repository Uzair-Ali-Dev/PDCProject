from django.http import HttpResponse 
from django.shortcuts import render


def home(request):
    return render(request,"home.html")

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
            dit={'fname':line[0],'lname':line[0]}
            Array.append(dit)
        # print(request.POST.get("zipcode"))
        # list =[{'fname':'abc', 'lname':'cadsad', 'cnic':'321321-21312-231'},{'fname':'abfdsfsdc', 'lname':'cadsafsdfdsd', 'cnic':'34321321-21312-231'}]
        dict={'list':Array}
        return render(request,"userDetails.html", dict)
    return render(request,"userDetails.html")
