def lu(l_1,l_2,l_3):
    l=[[1,0,0],
    [(l_2[0]/l_1[0]),1,0],
    [(l_3[0]/l_1[0]),(l_3[1]-(l_3[0]/l_1[0])*l_1[1])/(l_2[1]-((l_2[0]/l_1[0])*l_1[1])),0]]
    u=[l_1[:-1],
    [0,l_2[1]-(l[1][0]*l_1[1]),l_2[2]-(l[1][0]*l_1[2])],
    [0,0,l_3[2]-((l[2][0]*l_1[2])+(l[2][1]*(l_2[2]-(l[1][0]*l_1[2]))))]]
    print(l)
    print(u)
    return 1


    # for i in range(len(x_list)):
    #     print(x_list[i],y_list[i],z_list[i])
    # return x_list,y_list,z_list


if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    z_list=list(map(float,input("enter a list of z knot value :: ").split(" ")))
    x=lu(x_list, y_list, z_list)