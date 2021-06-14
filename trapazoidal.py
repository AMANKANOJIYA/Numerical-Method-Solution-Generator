import math

def functionToWork(x):
    y=1/(1+x)
    return y

# Trapazoid
def trapazoidal(x,y,itration):
    gap=(y-x)/itration
    create_x=[i*gap for i in range(0,itration+1)]
    create_y=[functionToWork(i) for i in create_x]
    formula=gap*(((create_y[0]+create_y[-1])/2)+sum([create_y[i] for i in range(1,len(create_y)-1)]))
    print(create_x)
    print(create_y)
    return formula


if __name__=="__main__":
    x,y=eval(input("Enter Lower Limit of the function:-> ")),eval(input("Enter Upper Limit of the Funcion:-> "))
    h=eval(input("Number of itrations :  "))
    e=trapazoidal(x,y,h)
    print(e,"this is your answer Trapazoidal")



