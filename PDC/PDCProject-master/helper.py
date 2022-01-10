def getRegionCount(regionList, data):
    # regionIndex is the array index where region name is stored
    regionIndex = 2

    for line in data:
        line = line.split("\t")
        regionList[line[regionIndex]] = regionList[line[regionIndex]] + 1

    return regionList


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
