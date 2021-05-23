def runga_func (x,y):
    function = x+(y**2) #You can change your function from here
    return function

# RungaKutta Method 
def rungaKutta (x_in,y_in,y_find,gap,itration=4):
    create_x=[i*gap for i in range(itration) ]
    create_y=[y_0]
    for i in range(itration):
        k_1 = gap * runga_func(create_x[i],create_y[-1])
        k_2 = gap * runga_func(create_x[i]+(gap/2),create_y[-1]+(k_1/2))
        k_3 = gap * runga_func(create_x[i]+(gap/2),create_y[-1]+(k_2/2))
        k_4 = gap * runga_func(create_x[i]+gap,create_y[-1]+k_3)
        k = (k_1+(2*k_2)+(2*k_3)+k_4)/6
        yOut = create_y[-1] + k
        create_y.append(yOut)
    return create_x,create_y


x_0 = eval(input("Enter the value of X-0 :=> "))
y_0 = eval(input("Enter the value of Y-0 :=> "))
find_y = eval(input("Enter the value of X_given :=> "))
itration = int(input("Number of itration if any else Type (0) :=> "))
gap = eval(input("FIll the gap between the sucessives  :=> "))
z, x = rungaKutta(x_0, y_0, find_y, gap, itration)
print(z,x)