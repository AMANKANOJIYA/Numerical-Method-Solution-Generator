import math
def runga_func (x,y):
    function = (y**2-x**2)/(y**2+x**2) #You can change your function from here
    return function

# RungaKutta Method 
def rungaKutta (x_in,y_in,gap,itration=4):
    create_x=[i*gap for i in range(itration) ]
    create_y=[y_in]
    print(create_x,"X table")
    print(create_y,"Y table\n\n")
    for i in range(itration):
        k_1 = gap * runga_func(create_x[i],create_y[-1])
        k_2 = gap * runga_func(create_x[i]+(gap/2),create_y[-1]+(k_1/2))
        k_3 = gap * runga_func(create_x[i]+(gap/2),create_y[-1]+(k_2/2))
        k_4 = gap * runga_func(create_x[i]+gap,create_y[-1]+k_3)
        k = (k_1+(2*k_2)+(2*k_3)+k_4)/6
        yOut = create_y[-1] + k
        create_y.append(yOut)
        print(f"k-1 : {k_1} , k-2 : {k_2} , k-3 : {k_3} , k-4 : {k_4} \n")
        print(f"k value {k} , y-output {yOut}\n\n")
    return create_x,create_y


x_0 = eval(input("Enter the value of X-0 :=> "))
y_0 = eval(input("Enter the value of Y-0 :=> "))
itration = int(input("Number of itration if any else Type (0) :=> "))
gap = eval(input("FIll the gap between the sucessives  :=> "))
z, x = rungaKutta(x_0, y_0, gap, itration)
print(z,x)