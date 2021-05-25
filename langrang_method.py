import numpy as np

def langrang(x_list,y_list,find_val):
    function=0
    for i in range(len(x_list)):
        list_up=[find_val-j for j in x_list if j!=x_list[i]]
        list_down=[x_list[i]-j for j in x_list if j!=x_list[i]]
        function=function+y_list[i]*(np.prod(list_up)/np.prod(list_down))
    return function

if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    find_val=eval(input("Enter the value to find :"))
    print(langrang(x_list, y_list, find_val))

    # 5 6 9 11
    # 12 13 14 16
    # 10