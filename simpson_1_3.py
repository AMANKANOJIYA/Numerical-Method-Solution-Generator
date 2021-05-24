x=list(map(float,input("enter a list of y knot value :: ").split(" ")))
h=eval(input("ENter the gap  :  "))
# simon 1/3
def simon_a(list_,h):
    formula=(h/3)*((list_[0]+list_[-1])+4*(sum([list_[i] for i in range(1,len(list_)-1,2)]))+2*(sum([list_[i] for i in range(2,len(list_)-1,2)])))
    return formula

if __name__=="__main__":
    e=simon_a(x,h)
    print(e,"this is your answer from simon 1/3")

# done