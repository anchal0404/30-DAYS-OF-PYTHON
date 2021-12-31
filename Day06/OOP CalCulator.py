import math
class calci:
    def __init__(self,p,q):
        self.p = p
        self.q = q
    
    def add(self):
        return self.p+self.q
     
    def sub(self):
        return self.p - self.q
    
    def multiply(self):
        return self.p * self.q
    
    def divide(self):
        return self.p / self.q
    
p=int(input("Enter I number:"))
q=int(input("Enter II number:"))

object=calci(p,q)
while True:
    def operation():
        u=('1. Add \n2. Sub \n3. Multiply \n4. Divide') 
        print(u)
    operation()
    perform=int(input('Select the operation to be perform'))
    
    if (perform==1):
        print("Solution:",object.add())
    elif (perform == 2):
        print("Result: ",object.sub())
    elif (perform == 3):
        print("Result: ",object.multiply())    
    elif (perform == 4):
        print("Result: ",object.divide())
    elif (perform == 0):
        print("Try operation")
    break

    

