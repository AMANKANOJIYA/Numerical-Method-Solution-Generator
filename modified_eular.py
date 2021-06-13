def eular_mod(x,y):
    function=x+y #you can change your function from here
    return function

x_0=eval(input("Enter the value of X-0 :=> "))
y_0=eval(input("Enter the value of Y-0 :=> "))
find_y=eval(input("Enter the value of X_given :=> "))
itration=int(input("Number of itration if any else Type (0) :=> "))
def eular_mod_calculation(x_0,y_0,y_giv,itration=1):
    gap=y_giv-x_0
    create_x=[i*gap for i in range(itration) ]
    create_y=[y_0]
    for i in range(1,itration):
        y_get=create_y[-1]+(gap*eular_mod(create_x[i],create_y[-1]))
        y_confirm=create_y[-1]+((gap/2)*(eular_mod(create_x[i],create_y[-1])+eular_mod(create_x[i]+gap,y_get)))
        create_y.append(y_confirm)
    for i in range(len(create_x)):
        print(f"x{i} = {create_x} , y{i} = {create_y}")
    return create_x,create_y

z,x=eular_mod_calculation(x_0,y_0,find_y,itration)
print(z,x)