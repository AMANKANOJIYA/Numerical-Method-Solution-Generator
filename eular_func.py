def eular(x,y):
    function=x+y #define your own function
    return function

x_0=eval(input("Enter the value of X-0 :=> "))
y_0=eval(input("Enter the value of Y-0 :=> "))
find_y=eval(input("Enter the value of Y_given :=> "))
itration=int(input("Number of itration if any else Type (0) :=> "))
def eular_calculation(x_0,y_0,y_giv,itration=6):
    gap=y_giv/(itration-1)
    create_x=[i*gap for i in range(itration) ]
    create_y=[y_0]
    for i in range(1,itration):
        y_get=create_y[-1]+(gap*eular(create_x[i],create_y[-1]))
        create_y.append(y_get)
    return create_x,create_y

z,x=eular_calculation(x_0,y_0,find_y,itration)
print(z,x)