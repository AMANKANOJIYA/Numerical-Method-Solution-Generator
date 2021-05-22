x=list(map(float,input("enter a list of y knot value :: ").split(" ")))
h=eval(input("ENter the gap  :  "))

# simon 3/8
def simon_b(list_,h):
    formula=((3*h)/8)*((list_[0]+list_[-1])+3*(sum([list_[i] for i in range(1,len(list_)) if (i)%3!=0]))+2*(sum([list_[i] for i in range(2,len(list_)-1,3)])))
    return formula

if __name__=="__main__":
    z=simon_b(x,h)
    print(z,"this is your answer from simon 3/8")