class Numerical_Analysis:
    """Numerical analysis, area of mathematics and computer science that creates,  
    analyzes, and implements algorithms for obtaining numerical solutions to  
    problems involving continuous variables. Such problems arise throughout the 
    natural sciences, social sciences, engineering, medicine, and business.
     
    In this Module We have Three Methods

>============ Eular Method =================<

    The Euler method is a first-order method, 
    which means that the local error (error per step) is  
    proportional to the square of the step size,  
    and the global error (error at a given time) is proportional  
    to the step size.

      Eular() 
      
    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform

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

>============ Eular Modified Method =================<

    listen) RUUNG-ə-KUUT-tah) are a family of implicit and explicit 
    iterative methods, which include the well-known routine called the 
    Euler Method, used in temporal discretization for the approximate 
    solutions of ordinary differential equations.

      RungaKutta()

    call this function to get Your Values 
    You can also pass Number Of itrations You Want to Perform

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<
     """
    def __init__(self,x_0,y_0,x_given):
        self.x_0=x_0
        self.y_0=y_0
        self.x_given=x_given
    def functionToWork(self,x,y):
        func=x+y
        return func
    def EularModified(self,itration=2):
        gap=self.x_given/(itration)
        create_x=[i*gap for i in range(itration+1) ]
        create_y=[self.y_0]
        for i in range(1,itration+1):
            y_get=create_y[-1]+(gap*self.functionToWork(create_x[i],create_y[-1]))
            y_confirm=create_y[-1]+((gap/2)*(self.functionToWork(create_x[i],create_y[-1])+self.functionToWork(create_x[i]+gap,y_get)))
            create_y.append(y_confirm)
        return create_x,create_y
    def Eular(self,itration=2):
        gap=self.x_given/(itration)
        create_x=[i*gap for i in range(itration+1) ]
        create_y=[self.y_0]
        for i in range(1,itration+1):
            y_get=create_y[-1]+(gap*self.functionToWork(create_x[i],create_y[-1]))
            create_y.append(y_get)
        return create_x,create_y
    def RungaKutta(self,itration=2):
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

>============ Trapazoid =================<

    Trapezoidal Rule is a rule that evaluates the area under 
    the curves by dividing the total area into smaller trapezoids 
    rather than using rectangles. This integration works by approximating 
    the region under the graph of a function as a trapezoid, 
    and it calculates the area.

      Trapazoid() 
      
    call this function to get Your Values 

>============ Simpson 1/3 =================<

    The trapezoidal rule was based on approximating the 
    integrand by a first order polynomial, and then integrating 
    the polynomial over interval of integration. Simpson’s 1/3 rule is an 
    extension of Trapezoidal rule where the integrand is approximated by a 
    second order polynomial.

      Simpson_13() 
      
    call this function to get Your Values 

>============ Simpson 3/8 =================<

    Simpson's 3/8 rule, also called Simpson's second rule 
    requests one more function evaluation inside the integration range,
    and is exact if f is a polynomial up to cubic degree.

      Simpson_38() 
      
    call this function to get Your Values 

>=========================================================<
|            Created By --- AMAN KANOJIYA                 |
>=========================================================<

    """
    def __init__(self):
        self.list=list(map(float,input("Enter a list of y knot value :: ").split(" ")))
        self.gap=eval(input("Enter the gap : "))
    
    def Trapazoid(self):
        formula=self.gap*(((self.list[0]+self.list[-1])/2)+sum([self.list[i] for i in range(1,len(self.list)-1)]))
        return formula
    
    def simpson_38(self):
        formula=((3*self.gap)/8)*((self.list[0]+self.list[-1])+3*(sum([self.list[i] for i in range(1,len(self.list)) if (i)%3!=0]))+2*(sum([self.list[i] for i in range(2,len(self.list)-1,3)])))
        return formula
    
    def Simpson_13(self):
        formula=(self.gap/3)*((self.list[0]+self.list[-1])+4*(sum([self.list[i] for i in range(1,len(self.list)-1,2)]))+2*(sum([self.list[i] for i in range(2,len(self.list)-1,2)])))
        return formula

if __name__=="__main__":
    x = Numerical_Analysis(0, 1, 0.1)
    print(x.Eular(5))
    print(x.EularModified(5))
    print(x.RungaKutta(5))

    y=Numerical_Integration()
    print(y.Trapazoid())
    print(y.simpson_13())
    print(y.simpson_38())
    # "1 0.972 0.9 0.8 0.692 0.5901 0.5",0.16666

