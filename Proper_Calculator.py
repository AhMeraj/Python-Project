import os
class calculator:
    a=0
    b=0
    result=0
    def Operation(self):
        self.a=float(input())
        while(True):
            self.c=str(input())
            self.b=float(input())
            if(self.c=='+'):
                self.result=self.Adding()
            elif (self.c == '-'):
                self.result = self.Subtraction()
            elif (self.c == '*'):
                self.result = self.Multiplication()
            elif (self.c == '/'):
                self.result = self.Division()
            else:
                print("Invalid Operation.")
            os.system('cls')
            self.Display();
            self.a=self.result;
    def Adding(self):
        return self.a+self.b
    def Subtraction(self):
        return self.a-self.b
    def Multiplication(self):
        return self.a*self.b
    def Division(self):
        return self.a/self.b
    def Display(self):
        print(self.result)
Hand=calculator()
Hand.Operation()