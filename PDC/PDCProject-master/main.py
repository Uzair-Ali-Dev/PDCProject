import os
import time

# args1 = {"operation": "getRegionData"}
args2 = {
    "operation": "getUserInfo",
    "params": {"zipCode": 102, "minAge": 0, "maxAge": 100},
}

start = time.time()

os.system('mpiexec -n 4 python script.py "' + str(args2) + '"')
print("<---->")
# os.system('mpiexec -n 3 python script.py "' + str(args2) + '"')

end = time.time()
print("Duration: ", end - start)
