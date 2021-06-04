def gause(l_1,l_2,l_3,itration):
    l_master=[l_1,l_2,l_3]
    for index,item in enumerate(l_master):
        for j in range(index):
            item=list(map(lambda x:(x*(l_master[0][index])-(x*(l_master[0][index]))) ,item))
        print(index,item)
    return 1


    # for i in range(len(x_list)):
    #     print(x_list[i],y_list[i],z_list[i])
    # return x_list,y_list,z_list


if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    z_list=list(map(float,input("enter a list of z knot value :: ").split(" ")))
    find_val=int(input("Define the number of itration :"))
    x=gause(x_list, y_list, z_list, find_val)