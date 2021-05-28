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
        
    index,gap=0,0
    for i in range(len(x_list)):
        print(x_find,x_list[i])
        if x_find<x_list[i]:
            index=x_list.index(x_list[i])
            gap=abs(x_list[i]-x_list[i-1])
            print(index,gap)
            break
    index,nochange_index=index-1,index
    u=(x_find-x_list[index])/gap
    function=0
    for x in range(len(overall)):
        print(index,(len(overall[0])-nochange_index))
        if x+1==1:
            function+=overall[x][index]
            print(function,"function")
        elif (index<(len(overall[0])-nochange_index) and (len(overall[0])-nochange_index)%2!=0):
            set=""
            for z in range(x):
                set+=(f"*(u-({z}))")
            print(set[1:],math.factorial(x),overall[x][nochange_index])
            function+=((eval(set[1:]))*overall[x][nochange_index])/math.factorial(x)
            print(function,"function")
        elif (index<=(len(overall[0])-nochange_index) and (len(overall[0])-nochange_index)%2==0):
            set=""
            for z in range(x):
                set+=(f"*(u-({z}))")
            print(set[1:],math.factorial(x),overall[x][nochange_index])
            function+=((eval(set[1:]))*overall[x][nochange_index])/math.factorial(x)
            print(function,"function")
        index+=1
    return function

if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    find_val=eval(input("Enter the value to find :"))
    print(Newton_Forward(x_list, y_list, find_val))