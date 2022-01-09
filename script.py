import helper as h
from mpi4py import MPI
import sys, json


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = []

print("Hello world from rank", str(rank), "of", str(size))
if rank == 0:
    # Reading Parameters
    args = sys.argv[1]
    args = args.replace("'", '"')
    options = json.loads(args)

    Areas = ["Shadman", "Garden", "DHA", "Bahria", "Nazimabad", "Defence"]
    rdata = {}
    for i in Areas:
        rdata[i] = 0

    # Reading Data from the file
    file = open("data.txt", "r")
    data = file.read().split("\n")
    file.close()
    print(data)

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

    # Sending the last chunk(remaining elements) to the last process
    i = i + 1
    index = i * chunk_size
    print("length: ", len(data))
    elements_left = len(data) - index
    comm.send(elements_left, dest=i)
    comm.send(data[index : index + elements_left], dest=i)
    comm.send(options, dest=i)
    if options["operation"] == "getRegionData":
        comm.send(rdata, dest=i)

    # Master processing its own set of data
    print("Master Here")
    if options["operation"] == "getRegionData":
        indiCount = h.getRegionCount(rdata, data[0:chunk_size])

    for i in range(0, chunk_size):
        print(data[i])

    # Receiving the results from the processes

    for i in range(1, size):
        ind = comm.recv(source=i)
        if options["operation"] == "getRegionData":
            for key in ind:
                indiCount[key] += ind[key]

    print("Master Count: ", indiCount)
    print("Master Done")
else:
    # Receiving the chunk size
    chunk_size = comm.recv(source=0)
    # Receiving data from master
    data = comm.recv(source=0)
    # Recieving options
    options = comm.recv(source=0)
    print("Chunk Size:", chunk_size)
    print("Length", len(data))

    if options["operation"] == "getRegionData":
        rdata = comm.recv(source=0)
        indiCount = h.getRegionCount(rdata, data)
        comm.send(indiCount, dest=0)

    for i in range(0, chunk_size):

        print(data[i])
