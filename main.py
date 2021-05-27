import numpy as np
class Numerical_Analysis:
    """Numerical analysis, area of mathematics and computer science that creates,  
    analyzes, and implements algorithms for obtaining numerical solutions to  
    problems involving continuous variables. Such problems arise throughout the 
    natural sciences, social sciences, engineering, medicine, and business.
     
    In this Module We have Three Methods
    ---> Eular mathod
    ---> Eular Modified method
    ---> Runga Kutta method

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<
     """
    def __init__(self,x_0,y_0,x_given):
        self.x_0=x_0
        self.y_0=y_0
        self.x_given=x_given
    def functionToWork(self,x,y):
        """
        This Help to generate The Function Output Given as per queestion 
        you can change this value for the code
        may be in next version you can see an another update so that
        the function can also be generated by the given user function input

            functionToWork(x,y)
        this function takes 2 input
        """
        func=1+((2*x*y)/1+(x**2))
        return func
    def EularModified(self,itration=2):
        """
    >============ Eular Modified Method =================<

    The objective in numerical methods is, as always, to achieve the most accurate (and reliable!) 
    result with the least effort.  
    For integrating the initial value problem (3)  
    the effort is usually measured by the number of times the function 
    $f(t,y)$ must be evaluated in stepping from $a$ to $b$. As we will see, 
    a simple improvement doubles the number of function evaluations per step, 
    but yields a second order method - a winning strategy.

      EularModified() 

    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform
        """
        gap=self.x_given/(itration)
        create_x=[i*gap for i in range(itration+1) ]
        create_y=[self.y_0]
        for i in range(1,itration+1):
            y_get=create_y[-1]+(gap*self.functionToWork(create_x[i],create_y[-1]))
            y_confirm=create_y[-1]+((gap/2)*(self.functionToWork(create_x[i],create_y[-1])+self.functionToWork(create_x[i]+gap,y_get)))
            create_y.append(y_confirm)
        return create_x,create_y
    def Eular(self,itration=2):
        """
    >============ Eular Method =================<

    The Euler method is a first-order method, 
    which means that the local error (error per step) is  
    proportional to the square of the step size,  
    and the global error (error at a given time) is proportional  
    to the step size.

      Eular() 
      
    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform
        """
        gap=self.x_given/(itration)
        create_x=[i*gap for i in range(itration+1) ]
        create_y=[self.y_0]
        for i in range(1,itration+1):
            y_get=create_y[-1]+(gap*self.functionToWork(create_x[i],create_y[-1]))
            create_y.append(y_get)
        return create_x,create_y
    def RungaKutta(self,itration=2):
        """
    >============ Eular Modified Method =================<

    listen) RUUNG-ə-KUUT-tah) are a family of implicit and explicit 
    iterative methods, which include the well-known routine called the 
    Euler Method, used in temporal discretization for the approximate 
    solutions of ordinary differential equations.

      RungaKutta()

    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform
        """
        gap=self.x_given/(itration)
        create_x=[i*gap for i in range(itration+1) ]
        create_y=[self.y_0]
        for i in range(itration):
            k_1 = gap * self.functionToWork(create_x[i],create_y[-1])
            k_2 = gap * self.functionToWork(create_x[i]+(gap/2),create_y[-1]+(k_1/2))
            k_3 = gap * self.functionToWork(create_x[i]+(gap/2),create_y[-1]+(k_2/2))
            k_4 = gap * self.functionToWork(create_x[i]+gap,create_y[-1]+k_3)
            k = (k_1+(2*k_2)+(2*k_3)+k_4)/6
            yOut = create_y[-1] + k
            create_y.append(yOut)
        return create_x,create_y

class Numerical_Integration:
    """
    Numerical integration methods can generally be described as combining 
    evaluations of the integrand to get an approximation to the integral. 
    The integrand is evaluated at a finite set of points called integration
    points and a weighted sum of these values is used to approximate 
    the integral.

    In this Module We have Three Methods
    ---> Trapazoid
    ---> Simpson 1/3
    ---> Simpson 3/8

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<

    """
    def __init__(self):
        self.x,self.y=eval(input("Enter Lower Limit of the Function:-> ")),eval(input("Enter Upper Limit of the Funcion:-> "))
        self.itration=eval(input("Number of itrations :  "))

    def Trapazoid(self):
        """
    >============ Trapazoid =================<

    Trapezoidal Rule is a rule that evaluates the area under 
    the curves by dividing the total area into smaller trapezoids 
    rather than using rectangles. This integration works by approximating 
    the region under the graph of a function as a trapezoid, 
    and it calculates the area.

      Trapazoid() 
      
    call this function to get Your Values 
    """
        def functionToWork(x):
            """
            This Help to generate The Function Output Given as per queestion 
            you can change this value for the code
            may be in next version you can see an another update so that
            the function can also be generated by the given user function input

                functionToWork(x)
            this function takes 1 input
            """
            return 1/(1+x**2)
        gap=(self.y-self.x)/self.itration
        create_x=[i*gap for i in range(0,self.itration+1)]
        create_y=[functionToWork(i) for i in create_x]
        formula=gap*(((create_y[0]+create_y[-1])/2)+sum([create_y[i] for i in range(1,len(create_y)-1)]))
        return formula
    
    def Simpson_38(self):
        """
    >============ Simpson 1/3 =================<

    The trapezoidal rule was based on approximating the 
    integrand by a first order polynomial, and then integrating 
    the polynomial over interval of integration. Simpson’s 1/3 rule is an 
    extension of Trapezoidal rule where the integrand is approximated by a 
    second order polynomial.

      Simpson_13() 
      
    call this function to get Your Values 

        """
        def functionToWork(x):
            """
            This Help to generate The Function Output Given as per queestion 
            you can change this value for the code
            may be in next version you can see an another update so that
            the function can also be generated by the given user function input

                functionToWork(x)
            this function takes 1 input
            """
            return 1/(1+x**2)
        gap=(self.y-self.x)/self.itration
        create_x=[i*gap for i in range(0,self.itration+1)]
        create_y=[functionToWork(i) for i in create_x]
        formula=((3*gap)/8)*((create_y[0]+create_y[-1])+3*(sum([create_y[i] for i in range(1,len(create_y)) if (i)%3!=0]))+2*(sum([create_y[i] for i in range(2,len(create_y)-1,3)])))
        return formula
    
    def Simpson_13(self):
        """
    >============ Simpson 3/8 =================<

    Simpson's 3/8 rule, also called Simpson's second rule 
    requests one more function evaluation inside the integration range,
    and is exact if f is a polynomial up to cubic degree.

      Simpson_38() 
      
    call this function to get Your Values 
        """
        def functionToWork(x):
            """
            This Help to generate The Function Output Given as per queestion 
            you can change this value for the code
            may be in next version you can see an another update so that
            the function can also be generated by the given user function input

                functionToWork(x)
            this function takes 1 input
            """
            return 1/(1+x**2)
        gap=(self.y-self.x)/self.itration
        create_x=[i*gap for i in range(0,self.itration+1)]
        create_y=[functionToWork(i) for i in create_x]
        formula=(gap/3)*((create_y[0]+create_y[-1])+4*(sum([create_y[i] for i in range(1,len(create_y)-1,2)]))+2*(sum([create_y[i] for i in range(2,len(create_y)-1,2)])))
        return formula

class Numerical_Interpolation:
    def __init__(self):
        self.x_l=list(map(float,input("enter a list of x knot value :: ").split(" ")))
        self.y_l=list(map(float,input("enter a list of y knot value :: ").split(" ")))
        self.find_val=eval(input("Enter the value to find :"))

    def Langrangian(self):
        function=0
        for i in range(len(self.x_l)):
            list_up=[self.find_val-j for j in self.x_l if j!=self.x_l[i]]
            list_down=[self.x_l[i]-j for j in self.x_l if j!=self.x_l[i]]
            function=function+self.y_l[i]*(np.prod(list_up)/np.prod(list_down))
        return function

    def Newton_Divided(self):
        length=len(self.x_l)
        overall=[self.y_l]
        x_gap=1
        def divisor(x_0,x_1,y_0,y_1):
            y=(y_1-y_0)/(x_1-x_0)
            return y
        for i in range(length,1,-1):
            local=[]
            y_list_itrate=overall[-1]
            for j in range(i-1):
                z=divisor(self.x_l[j], self.x_l[j+x_gap], y_list_itrate[j], y_list_itrate[j+1])
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
                    set=set+(f"*(self.find_val-({self.x_l[z]}))")
                function+=((overall[x][0])*(eval(set[1:])))
        return function

if __name__=="__main__":
    x = Numerical_Analysis(0, 1, 0.1)
    print(x.Eular(5))
    print(x.EularModified(5))
    print(x.RungaKutta(5))

    y=Numerical_Integration()
    print(y.Trapazoid())
    print(y.Simpson_13())
    print(y.Simpson_38())
    # "1 0.972 0.9 0.8 0.692 0.5901 0.5",0.16666

