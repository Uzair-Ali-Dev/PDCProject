from collections import UserList
import helper as h
from mpi4py import MPI
import sys, json


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = []

# print("Hello world from rank", str(rank), "of", str(size))
if rank == 0:
    # Reading Parameters
    args = sys.argv[1]
    args = args.replace("'", '"')
    options = json.loads(args)
    usersList = []
    zipNames={}
    
    zipCodes=[
    "75850",	
    "74700",	
    "75760",	
	"75990",	
	"75700",	
	"75900",	
	"75890",	
	"75840",	
 	"74600",	
	"75790",	
	"75850",	
	"75800",	
	"74000",	
	"75650",	
	"75660",	
	"75750",	
	"75780",	
	"75730",	
	"75600",	
    "74200",	
	"75580",	
	"75520",	
	"75620",	
	"75640",	
	"75530",	
	"75500",
	"75510",	
    "74400",	
    "75950",	
 	"75290",	
 	"75300",	
 	"75260",	
	"75330",	
	"75280",	
	"75340",	
	"75550",	
	"75400",	
	"75350",	
 	"75270",	
 	"75460",	
	"74800"]
    # zipCodes = ["101", "102", "103", "104", "105", "106"]
    
    totalCount={}
    rdata = {}
    for i in zipCodes:
        rdata[i] = 0
        totalCount[i]=0

    # Reading Data from the file
    file = open("PDCProject-master/areazipcode.txt", "r")
    data = file.read().split("\n")
    file.close()
    for i in data:
        line=i.split("\t")
        zipNames[line[1]]=line[0]
    # print(zipNames)
    file = open("PDCProject-master/data2.txt", "r")
    data = file.read().split("\n")
    file.close()
    # print(data)

    # Getting the chunk size
    chunk_size = len(data) // size

    # Splitting the data into chunks and sending to processes
    for i in range(1, size - 1):
        index = i * chunk_size
        comm.send(chunk_size, dest=i)
        comm.send(data[index : index + chunk_size], dest=i)
        comm.send(options, dest=i)

        if options["operation"] == "getRegionData":
            comm.send(rdata, dest=i)
            comm.send(totalCount, dest=i)

    # Sending the last chunk(remaining elements) to the last process
    i = i + 1
    index = i * chunk_size
    # print("length: ", len(data))
    elements_left = len(data) - index
    comm.send(elements_left, dest=i)
    comm.send(data[index : index + elements_left], dest=i)
    comm.send(options, dest=i)
    if options["operation"] == "getRegionData":
        comm.send(rdata, dest=i)
        comm.send(totalCount, dest=i)
    # elif options["operation"] == "getUserInfo":
    #     comm.send(rdata, dest=i)
    # Master processing its own set of data
    print("Master Here")
    if options["operation"] == "getRegionData":
        result = h.getRegionCount(totalCount,rdata, data[0:chunk_size])
        indiCount=result["pCount"]
        tCount=result["totalCount"]
    elif options["operation"] == "getUserInfo":
        userDetails = h.getUserDetails(data[0:chunk_size], options["params"])
        print("User Details master---------------------------: ",len(userDetails))
        for i in userDetails:
            usersList.append(i)

        # Receiving the results from the processes

        # print("User Details Master: ", userDetails)
        
    # for i in range(0, chunk_size):
    #     print(data[i])



    # Receiving the results from the processes

    if options["operation"] == "getRegionData":
        for i in range(1, size):
            ind = comm.recv(source=i)
            tC=comm.recv(source=i)
            for key in ind:
                indiCount[key] += ind[key]
            for key in tC:
                totalCount[key] += tC[key]

        print("Master Count positive: ", indiCount)
        print("Master Count all: ", totalCount)
        file = open("PDCProject-master/temp.txt", "w")
        # print("------",zipNames)
        
        for key,value in indiCount.items():
            # print(key ,value)
            file.write(str(key) +"\t"+str(zipNames[str(key)])+ "\t" + str(value) +"\t"+ str(totalCount[key])+"\n")
        # file.write("\b")
        file.close()


    if options["operation"] == "getUserInfo":
        for i in range(1, size):
            result = comm.recv(source=i)
            for j in result:
                usersList.append(j)
            # print("Result: ", result)

        print("User Details---------------------------: ",len(usersList))
        file = open("PDCProject-master/temp.txt", "w")
        for i in usersList:
            # print(key ,value)
            # dict={'Name':line[0],'Age':age,'Cnic':line[2],'Gender':line[3],'Street':line[5],'ZipCode':line[6],'Vaccinestatus':line[7],'CovidStatus':line[8]}
            file.write(str(i["Name"]) +"\t"+str(i["Age"])+ "\t" + str(i["Cnic"]) +"\t"+ str(i["Gender"])+"\t"+ str(i["Street"])+"\t"+ str(i["ZipCode"])+"\t"+ str(i["Vaccinestatus"])+"\t"+ str(i["CovidStatus"])+ "\n")
        # file.write("\b")
        file.close()
    print("Master Done")
else:
    # Receiving the chunk size
    chunk_size = comm.recv(source=0)
    # Receiving data from master
    data = comm.recv(source=0)
    print("child data---------------------------: ",len(data),rank)
    # Recieving options
    options = comm.recv(source=0)
    # print("Chunk Size:", chunk_size)
    # print("Length", len(data))

    if options["operation"] == "getRegionData":
        rdata = comm.recv(source=0)
        totalCount = comm.recv(source=0)
        result = h.getRegionCount(totalCount,rdata, data)
        indiCount=result["pCount"]
        tCount=result["totalCount"]
        comm.send(indiCount, dest=0)
        comm.send(tCount, dest=0)

    elif options["operation"] == "getUserInfo":
        userDetails = h.getUserDetails(data, options["params"] )
        print("User Details child---------------------------: ",len(userDetails),rank)
        comm.send(userDetails, dest=0)

    # for i in range(0, chunk_size):
        # print(data[i])
