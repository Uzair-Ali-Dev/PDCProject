from datetime import date
from mpi4py import MPI
# from types import NoneType
def getRegionCount(totalCount,regionList, data):
    # regionIndex is the array index where region name is stored
    regionIndex = 6
    covidStatusIndex=8
    for line in data:
        line = line.split("\t")
        if str(line[8])=="positive":
            regionList[line[regionIndex]] = regionList[line[regionIndex]] + 1
            totalCount[line[regionIndex]]= totalCount[line[regionIndex]] +1
        else:
            totalCount[line[regionIndex]]= totalCount[line[regionIndex]] +1

    dict={"pCount":regionList,"totalCount":totalCount}
    return dict


def getUserDetails(data, options):

    zipCodeIndex = 6
    # ageIndex = 1

    zipCode = options["zipCode"]
    minAge = int(options["minAge"])
    maxAge = int(options["maxAge"])

    userDetails = []
    for line in data:
        line = line.split("\t")
        bdate=line[1].split("-")
        today = date.today()
        age=today.year - int(bdate[0]) - ((today.month, today.day) < (int(bdate[1]), int(bdate[2])))
        if (zipCode == ""):
            if (age >= minAge and age <= maxAge):

                dict={'Name':line[0],'Age':age,'Cnic':line[2],'Gender':line[3],'Street':line[5],'ZipCode':line[6],'Vaccinestatus':line[7],'CovidStatus':line[8]}
                userDetails.append(dict)
            # int(line[ageIndex]) >= minAge
            # int(line[ageIndex]) <= maxAge
        if (line[zipCodeIndex] == str(zipCode)and age >= minAge and age <= maxAge):
            # comm.abort()
            dict={'Name':line[0],'Age':age,'Cnic':line[2],'Gender':line[3],'Street':line[5],'ZipCode':line[6],'Vaccinestatus':line[7],'CovidStatus':line[8]}
            userDetails.append(dict)


    return userDetails
