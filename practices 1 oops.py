class calculator:
    def __init__(self,n):
        self.n = n 

    def square(self):
        print(f"the square of is = {self.n*self.n}")
    def cube(self):
        print(f"the cube is = {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the squarerrot is = {self.n**0.5} ")


a = calculator(16)
a.square()
a.cube()
a.squareroot()

    