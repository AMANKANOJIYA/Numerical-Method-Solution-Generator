
def gause_seidle(l_1,l_2,l_3,itration):
    x_list=[0]
    y_list=[0]
    z_list=[0]
    for i in range(itration):
        x,y,z=x_list[-1],y_list[-1],z_list[-1]
        x_find=(l_1[-1]-((l_1[1])*(y))-((z)*(l_1[2])))/l_1[0]
        y_find=(l_2[-1]-((l_2[0])*(x_find))-((z)*(l_2[2])))/l_2[1]
        z_find=(l_3[-1]-((l_3[0])*(x_find))-((y_find)*(l_3[1])))/l_3[2]
        x_list.append(x_find)
        y_list.append(y_find)
        z_list.append(z_find)
    for i in range(len(x_list)):
        print(x_list[i],y_list[i],z_list[i])
    return x_list,y_list,z_list


def gause_seidle_4(l_1,l_2,l_3,l_4,itration):
    x_list=[0]
    y_list=[0]
    z_list=[0]
    w_list=[0]
    for i in range(itration):
        x,y,z,w=x_list[-1],y_list[-1],z_list[-1],w_list[-1]
        x_find=(l_1[-1]-((l_1[1])*(y))-((z)*(l_1[2]))-((w)*(l_1[3])))/l_1[0]
        y_find=(l_2[-1]-((l_2[0])*(x_find))-((z)*(l_2[2]))-((w)*(l_2[3])))/l_2[1]
        z_find=(l_3[-1]-((l_3[0])*(x_find))-((y_find)*(l_3[1]))-((w)*(l_3[3])))/l_3[2]
        w_find=(l_4[-1]-((l_4[0])*(x_find))-((y_find)*(l_4[1]))-((z_find)*(l_4[2])))/l_4[3]
        x_list.append(x_find)
        y_list.append(y_find)
        z_list.append(z_find)
        w_list.append(w_find)
    for i in range(len(x_list)):
        print(x_list[i],y_list[i],z_list[i],w_list[i])
    return x_list,y_list,z_list,w_list


if __name__=="__main__":
    x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
    y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
    z_list=list(map(float,input("enter a list of z knot value :: ").split(" ")))
    w_list=list(map(float,input("enter a list of w knot value :: ").split(" ")))
    find_val=int(input("Define the number of itration :"))
    # x,y,z=gause_seidle(x_list, y_list, z_list, find_val)

    x,y,z,w=gause_seidle_4(x_list,y_list,z_list,w_list,find_val)

#     twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ 
# dist/*