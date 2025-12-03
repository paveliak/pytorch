import torch
if torch.backends.mps.is_available():
    device = torch.device("mps")
    x = torch.ones(1, device=device)
    print (x)
else:
    print ("MPS device not found.")

import math
def add(dtype):
    x = torch.ones(5, device=device, dtype=dtype)
    y = torch.ones(5, device=device, dtype=dtype)
    r = x + y
   # print(r)
    print(x)
    print(torch.abs(r))
add(torch.float)
add(torch.bfloat16)
add(torch.half)
#add(torch.int)
