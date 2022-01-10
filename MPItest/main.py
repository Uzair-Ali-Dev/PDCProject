import os, json
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
# print("Hello world from rank", str(rank), "of", str(size))

# args = {'"operation"':'"getRegionData"','"params"':{'"id"':1, '"zipCode"':123}}
# args = {"\'operation\'":"\'getRegionData\'","\'params\'":{"\'id\'":1, "\'zipCode\'":123}}
# a= {"abc":123}
args = {"operation":"getRegionData","params":{"id":1, "zipCode":123}}
# print(json.dumps(args))
# args=json.dumps(args)
# print(args)
# os.system("python scr.py \'"+str(args)+"\'")

os.system("mpiexec -n 4 python script.py \'"+str(args)+"\'")