x=list(map(float,input("enter a list of y knot value :: ").split(" ")))
h=eval(input("ENter the gap  :  "))

# Trapazoid
def trapazoidal(list_,h):
    formula=h*(((list_[0]+list_[-1])/2)+sum([list_[i] for i in range(1,len(list_)-1)]))
    return formula


if __name__=="__main__":
    f=trapazoidal(x,h)
    print(f,"this is your answer from trapazoidal")



