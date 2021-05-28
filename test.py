class none:
    def sun(x,y):
        return x+y
    def rome(self,x,y):
        z=0
        for i in range(0,x+y):
            z=none.sun(z,i)
            # z=self.sun(z,i) if self is used
        return z
# z=none()
# print(z.rome(32,32))

x=[1,2,3,4,5,6,78,3]
print(x.index(78))


