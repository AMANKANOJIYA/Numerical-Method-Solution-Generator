# x=list(map(float,input("enter a list of y knot value :: ").split(" ")))
x,y=eval(input("Enter Lower Limit of the function:-> ")),eval(input("Enter Upper Limit of the Funcion:-> "))
h=eval(input("Number of itrations :  "))
# simon 1/3
def function(x):
    y=1/(1+x**2)
    return y

def simpson_a(x,y,itration):
    gap=(y-x)/itration
    create_x=[i*gap for i in range(0,itration+1)]
    create_y=[function(i) for i in create_x]
    formula=(gap/3)*((create_y[0]+create_y[-1])+4*(sum([create_y[i] for i in range(1,len(create_y)-1,2)]))+2*(sum([create_y[i] for i in range(2,len(create_y)-1,2)])))
    return formula

if __name__=="__main__":
    e=simpson_a(x,y,h)
    print(e,"this is your answer from simpson 1/3")

# done