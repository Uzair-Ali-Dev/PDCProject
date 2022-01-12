from datetime import date
from mpi4py import MPI

# from types import NoneType
def getRegionCount(vaccinationCount, totalCount, regionList, data):
    # regionIndex is the array index where region name is stored
    regionIndex = 6
    covidStatusIndex = 8
    for line in data:
        line = line.split("\t")
        if str(line[7]) == "vaccinated":
            vaccinationCount[line[regionIndex]] = (
                vaccinationCount[line[regionIndex]] + 1
            )
        if str(line[8]) == "positive":
            regionList[line[regionIndex]] = regionList[line[regionIndex]] + 1 #covid positive
            totalCount[line[regionIndex]] = totalCount[line[regionIndex]] + 1
        else:
            totalCount[line[regionIndex]] = totalCount[line[regionIndex]] + 1

    dict = {
        "vaccinationCount": vaccinationCount,
        "pCount": regionList,
        "totalCount": totalCount,
    }
    return dict


def getUserDetails(data, options, comm):

    zipCodeIndex = 6
    # ageIndex = 1

    zipCode = options["zipCode"]
    minAge = int(options["minAge"])
    maxAge = int(options["maxAge"])
    cnic = options["cnic"]
    gender = int(options["gender"])
    print("cnic rank", cnic, comm.rank)
    print("gender", gender)
    userDetails = []

    if cnic != "":
        for line in data:
            # for k in range(0, comm.size):
                # if comm.irecv(None, source=k):
                #     break
            line = line.split("\t")
            bdate = line[1].split("-")
            today = date.today()
            age = (
                today.year
                - int(bdate[0])
                - ((today.month, today.day) < (int(bdate[1]), int(bdate[2])))
            )
            if line[2] == str(cnic):
                print("Data Found", cnic, comm.rank)
                dict = {
                    "Name": line[0],
                    "Age": age,
                    "Cnic": line[2],
                    "Gender": line[3],
                    "Street": line[5],
                    "ZipCode": line[6],
                    "Vaccinestatus": line[7],
                    "CovidStatus": line[8],
                }
                userDetails.append(dict)
                # for j in range(0, comm.size):
                #     if j != comm.rank:
                #         comm.isend("found", dest=j)
                #     break
    else:
        for line in data:
            line = line.split("\t")
            bdate = line[1].split("-")
            today = date.today()
            age = (
                today.year
                - int(bdate[0])
                - ((today.month, today.day) < (int(bdate[1]), int(bdate[2])))
            )
            if zipCode == "":
                if age >= minAge and age <= maxAge:
                    if gender != 0:

                        if gender == 1:
                            cGender = "M"
                        else:
                            cGender = "F"

                        if str(line[3]) == cGender:
                            dict = {
                                "Name": line[0],
                                "Age": age,
                                "Cnic": line[2],
                                "Gender": line[3],
                                "Street": line[5],
                                "ZipCode": line[6],
                                "Vaccinestatus": line[7],
                                "CovidStatus": line[8],
                            }
                            userDetails.append(dict)
                    else:
                        dict = {
                            "Name": line[0],
                            "Age": age,
                            "Cnic": line[2],
                            "Gender": line[3],
                            "Street": line[5],
                            "ZipCode": line[6],
                            "Vaccinestatus": line[7],
                            "CovidStatus": line[8],
                        }
                        userDetails.append(dict)

            if line[zipCodeIndex] == str(zipCode) and age >= minAge and age <= maxAge:
                if gender != 0:

                    if gender == 1:
                        cGender = "M"
                    else:
                        cGender = "F"

                    if str(line[3]) == cGender:
                        dict = {
                            "Name": line[0],
                            "Age": age,
                            "Cnic": line[2],
                            "Gender": line[3],
                            "Street": line[5],
                            "ZipCode": line[6],
                            "Vaccinestatus": line[7],
                            "CovidStatus": line[8],
                        }
                        userDetails.append(dict)
                else:
                    dict = {
                        "Name": line[0],
                        "Age": age,
                        "Cnic": line[2],
                        "Gender": line[3],
                        "Street": line[5],
                        "ZipCode": line[6],
                        "Vaccinestatus": line[7],
                        "CovidStatus": line[8],
                    }
                    userDetails.append(dict)

    return userDetails
