import os
import time

args = {"operation": "getRegionData", "params": {"id": 1, "zipCode": 123}}


start = time.time()

os.system('mpiexec -n 4 python script.py "' + str(args) + '"')

end = time.time()
print("Duration: ", end - start)
