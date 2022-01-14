
import numpy as np
from math import sqrt

B =  {
    "x":2,
    "y":4,
    "z":0
}

def M(t):
    return {
        "x":3+t,
        "y":6*t,
        "z":-3*t
    }

# range for floats with np.arange()
for i in np.arange(0.45,0.55, 0.01):
    m = M(i)
    b = B
    vBM = [(m["x"]-B["x"]),(m["y"]-B["y"]),(m["z"]-B["z"])]
    print("Pour t : ",i,"\nDistance : ",sqrt((vBM[0]**2)+(vBM[1]**2)+(vBM[2]**2)))

