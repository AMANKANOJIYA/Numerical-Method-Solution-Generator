# import math
# import sympy as sp
# def Newton_Forward(x_list,y_list,x_find):
#     length=len(x_list)
#     overall=[y_list]
#     x_gap=1
#     for i in range(length,1,-1):
#         local=[]
#         y_list_itrate=overall[-1]
#         for j in range(i-1):
#             z=y_list_itrate[j+1] - y_list_itrate[j]
#             local.append(z)
#         overall.append(local)
#         x_gap+=1

#     z=len(overall)//2 
#     for i in range(len(overall)):
#         for index in range(len(overall[i])):
#             print(f"{index}y_{i}=",round(overall[index][i],4),end="  ")
#         print("\n ")

    
#     function=0
#     index_,fix=x_list.index(x_find),x_list.index(x_find)
#     for x in range(len(overall)):
#         if x+1==1:
#             function+=overall[x][0]
#         elif(index_<=len(x_list) and index_>=0) :
#             set=""
#             for z in range(x):
#                 set+=(f"*(u-({z}))")
#             u=sp.Symbol("u")
#             diri=str(eval(set[1:]).diff(u))
#             u=0
#             print(set[1:] ,"--set    diri--", diri)
#             print(index_)
#             function+=((1/(x_list[1]-x_list[0]))*((eval(diri))*overall[x][index_])/math.factorial(x))
#         index_=index_-1
#     return function

# if __name__=="__main__":
#     x_list=list(map(float,input("enter a list of x knot value :: ").split(" ")))
#     y_list=list(map(float,input("enter a list of y knot value :: ").split(" ")))
#     find_val=eval(input("Enter the value to find :"))
#     print(f"The Corresponding y Value for {find_val} is : {Newton_Forward(x_list, y_list, find_val)} ")


# import math
# x=0.25
# y=0
# gap=0.1
# a=eval("x+y**3")
# a=eval("3*x+4*x")
# print(a)
# print(math.e) #2.718281828459045
# math.sqrt(math.log(x))


# def aman(*args):
#     sum=0
#     args=args[0]
#     for i in args:
#         print(i**2)
#         sum+=i**2
#     return sum


# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=aman, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))



# def Error_maintain(x,y,oper):
#     try:
#         val=eval(oper)
#         return val
#     except Exception as e:
#         return f"Error {e} aram se"


# def add(x,y):
#     return Error_maintain(x,y,"x+y")
# def sub(x,y):
#     return Error_maintain(x,y,"x-y")
# def multi(x,y):
#     return Error_maintain(x,y,"x*y")
# def div(x,y):
#     return Error_maintain(x,y,"x/y")
# def mod(x,y):
#     return Error_maintain(x,y,'x%y')
# def pow(x,y):
#     return Error_maintain(x,y,"x**y")
# print(add(40,34))
# print(sub(40,40))
# print(multi(40,40))
# print(div(40,40))
# print(mod(40,40))
# print(pow(40,40))


# def decor(func):
#     def inner():
#         print("this is a function - 1")
#         func()
#         print("this is a function - 3")
#     return inner
# def decor2(func):
#     def inner():
#         print("this is a function - 1000")
#         func()
#         print("this is a function - 3000")
#     return inner

# @decor
# def main ():
#     print("This is A function - 2 ")

# @decor
# def main2():
#     print("Go")

# main()
# main2()



# def Error_Handler(func):
#     def Inner_Function(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         # except TypeError:
#         #     print(f"Any Variable Have wrong data types. \n Please Check The respective data types as the parameter acceptes \n for help you can use `  help({func.__name__})  ` to get More detailed use of it")
#         except ZeroDivisionError:
#             print(f"{func.__name__} contanin variables are Generating Zero Division Error \n Please Check All the values Provided \n for help you can use `  help({func.__name__})  ` to get More detailed use of it")
#         except Exception as e :
#             print(f"{e} \n for help you can use `  help({func.__name__})  ` to get More detailed use of it")
#     return Inner_Function



# @Error_Handler
# def Mean(a,b):
#         print((a+b)/2)
      
# @Error_Handler
# def Square(sq):
#         print(sq*sq)
  
# @Error_Handler
# def Divide(l,b):
#         print(b/l)
      
# Mean(4,5)
# Square(14)
# Divide(8)
# Square("three")
# Divide("two","one")
# Mean("six","five")

def Error_Handler(func):
    def inner (*args):
        try:
            func(*args)
            print(func.__name__)
        except Exception as e:
            print(f"{type(e).__name__}\n==============\n {e} \n in{func.__name__} function")
    return inner

class general():
    @Error_Handler
    def __init__(self, x,y,z):
        self.x=int(x)
        self.y=int(y)
        self.z=int(z)

    @Error_Handler
    def extra(self,we,ze):
        print(we,ze)

x=general(234234, "asd" ,234)
x.extra(234, 32423)
        





