

import numpy as np
import math

# simon 1/3
def function(x):
    y=math.sqrt(np.cos(x))
    return y

# simpson 3/8
def simpson_b(x,y,itration):
        gap=(y-x)/itration
        create_x=[i*gap for i in range(0,itration+1)]
        create_y=[function(i) for i in create_x]
        formula=((3*gap)/8)*((create_y[0]+create_y[-1])+3*(sum([create_y[i] for i in range(1,len(create_y)) if (i)%3!=0]))+2*(sum([create_y[i] for i in range(2,len(create_y)-1,3)])))
        print(create_x)
        print(create_y)
        return formula
if __name__=="__main__":
    x,y=eval(input("Enter Lower Limit of the function:-> ")),eval(input("Enter Upper Limit of the Funcion:-> "))
    h=eval(input("Number of itrations :  "))
    e=simpson_b(x, y, h)
    print(e,"this is your answer simposn 3/8")