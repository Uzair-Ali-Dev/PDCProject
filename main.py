import os
import time

args1 = {"operation": "getRegionData"}
# args2 = {
#     "operation": "getUserInfo",
#     "params": {"zipCode": 11, "minAge": 0, "maxAge": 16},
# }

start = time.time()

os.system('mpiexec -n 4 python script.py "' + str(args1) + '"')
# os.system('mpiexec -n 4 python script.py "' + str(args2) + '"')

end = time.time()
print("Duration: ", end - start)
