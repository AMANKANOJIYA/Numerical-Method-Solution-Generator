def divisor(x_0,x_1,y_0,y_1):
    y=(y_1-y_0)/(x_1-x_0)
    return y
def Newton_Divided(x_list,y_list,x_find):
    length=len(x_list)
    overall=[y_list]
    x_gap=1
    for i in range(length,1,-1):
        local=[]
        y_list_itrate=overall[-1]
        for j in range(i-1):
            z=divisor(x_list[j], x_list[j+x_gap], y_list_itrate[j], y_list_itrate[j+1])
            local.append(z)
        overall.append(local)
        x_gap+=1
    function=0
    for x in range(len(overall)):
        if x+1==1:
            function+=overall[x][0]
        else:
            set=""
            for z in range(x):
                set=set+(f"*(x_find-({x_list[z]}))")
            function+=((overall[x][0])*(eval(set[1:])))
    return function

if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    find_val=eval(input("Enter the value to find :"))
    print(Newton_Divided(x_list, y_list, find_val))