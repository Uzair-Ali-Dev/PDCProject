def getRegionCount(regionList, data):
    regionIndex = 2
    print("Inside Data: ", data)
    for line in data:
        line = line.split("\t")
        regionList[line[regionIndex]] = regionList[line[regionIndex]] + 1

    return regionList
