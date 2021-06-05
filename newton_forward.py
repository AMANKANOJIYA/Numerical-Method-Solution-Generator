import math
def Newton_Forward(x_list,y_list,x_find):
    length=len(x_list)
    overall=[y_list]
    x_gap=1
    for i in range(length,1,-1):
        local=[]
        y_list_itrate=overall[-1]
        for j in range(i-1):
            z=y_list_itrate[j+1] - y_list_itrate[j]
            local.append(z)
        overall.append(local)
        x_gap+=1

    z=len(overall)//2 
    for i in range(len(overall)):
        for index in range(len(overall[i])):
            print(f"{index}y_{i}=",round(overall[index][i],4),end="  ")
        print("\n ")

    u=(x_find-x_list[0])/(x_list[1]-x_list[0])
    function=0
    for x in range(len(overall)):
        if x+1==1:
            function+=overall[x][0]
        else :
            set=""
            for z in range(x):
                set+=(f"*(u-({z}))")
            function+=((eval(set[1:]))*overall[x][0])/math.factorial(x)
    return function

if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    find_val=eval(input("Enter the value to find :"))
    print(f"The Corresponding y Value for {find_val} is : {Newton_Forward(x_list, y_list, find_val)} ")