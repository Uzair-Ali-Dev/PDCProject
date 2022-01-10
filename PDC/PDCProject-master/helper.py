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

    zipCodeIndex = 2
    ageIndex = 1

    zipCode = options["zipCode"]
    minAge = options["minAge"]
    maxAge = options["maxAge"]

    userDetails = []
    for line in data:
        line = line.split("\t")
        if (zipCode == ""):
            pass
            # int(line[ageIndex]) >= minAge
            # int(line[ageIndex]) <= maxAge

        if (
            line[zipCodeIndex] == str(zipCode)
            and int(line[ageIndex]) >= minAge
            and int(line[ageIndex]) <= maxAge
        ):
            userDetails.append(line)


    return userDetails
