import os
import sys

class Equation:
    def __init__(self, Eq):
        self.eq = "".join(x for i,x in enumerate(Eq) if i != 0)
        self.listString = [x for x in Eq]

        #print(self.listString)
        self.checkNext = False

        self.n = ""
        self.p = ""
        self.o = ""
        self.values = []
        self.calcPow = False
        self.calculate()

    def calculate(self):
        for i,x in enumerate(self.listString):
            #IsCheckingNumber + IsCheckingNumber?
            if self.calcPow == False:
                if (self.checkNext == True):
                    #add current value cause it's a number
                    self.n += x
                    try:
                        self.listString[i+1]
                        try:
                            int(self.listString[i+1])
                        except:
                            #if number is not an intable value doesn't check anymore
                            if self.listString[i+1] != ".":
                                self.checkNext = False
                                self.calcPow = True
                    except:
                        self.p = "0"
                        self.setVal()

                #StartCheckingNumber?
                if (x == '+' or x == '-'):
                    self.o = x
                    try:
                        int(self.listString[i+1])
                        self.checkNext = True
                    except:
                        self.n = "1"
            else:
                #IsCheckingPower + IsCheckingPower?
                if x != "^" and self.checkNext:
                    self.p += x
                    try:
                        int(self.listString[i+1])
                    except:
                        if self.listString[i+1] != ".":
                            self.setVal()
                #If value is x then start checking for powers
                elif x == "x":
                    #check if next val exists
                    try:
                        #if exists then start checking the full number
                        if self.listString[i+1] == "^":
                            self.checkNext = True
                        
                        #otherwise set it to one and call setval
                        else:
                            self.p = "1"
                            self.setVal()
                    except:
                        self.p = "1"
                        self.setVal()
                #if value + or - instead of x set power to 0 and call setVal and afterwards do the check usually done in numbers section
                elif x == '+' or x == '-':
                    self.o = x
                    self.p = "0"
                    self.setVal()
                    try:
                        int(self.listString[i+1])
                        self.checkNext = True
                    except:
                        self.n = "1"
            #if calcPow == true if x = "x" if next value is "^" then continue finding else set pow as one if x = + or x = - then set pow as 0

        return [x.__str__() for x in self.values]
    
    def setVal(self):
        self.values.append(Value(self.n,self.p, self.o))
        self.n, self.p, self.o = "","", ""
        self.calcPow = False
        self.checkNext = False
    
    def check(self):
        x = input("Choose an index to check from 0 to {}: \n".format(len(self.values)-1))
        try: 
            int(x)
            return self.values[int(x)].__str__()
        except:
            pass

    #when start checking operator fet values of powers from Value isntead
    def findY(self):
        try:
            x = float(input("What is the value for x which you want to find?\n"))
            result = 0
            for value in self.values:
                result += float(value.o+value.n)*x**float(value.p)
            return result
        except:
            os.system('clear')
            print("The Equation is {}\n=============================\n".format(self.eq))
            print("Choose a valid value please.\n")
            self.findY()

    def __str__(self):
        return self.eq
    
class Value:
    def __init__(self, N, P, O):
        #number
        self.n = N
        #operator
        self.o = O
        #power
        self.p = P
    def __str__(self):
        return "Number: {}, Power: {}".format(str(float(self.o+self.n)),self.p)

#given = "35.45x^22.25+3+32x-3"
def main():
    os.system('clear')
    given = input("Equation: ")


    possible = "0123456789-+x."
    equation = ""
    isPossible = False
    #eq = "".join(x for x in given if (x != y for y in possible))
    for i in given:
        for j in possible:
            if(i == j):
                isPossible = True
        if isPossible:
            equation += i 
        isPossible = False
    os.system('clear')                
    print("The Equation is {}\n=============================\n".format(equation))

    try:
        int(equation[0])
        equation = "+" + equation
    except:
        pass

    eq = Equation(equation)

    while True:
        instruct = input("0: Check the values for specific index.\n1: Find y value for a certain x value.\n2: Exit\nAction: ")
        os.system('clear')
        
        print("The Equation is {}\n=============================\n".format(eq))

        if instruct == "0":
            print(eq.check())
        elif instruct == "1":
            print(eq.findY())
        elif instruct == "2":
            os.system('clear')
            sys.exit()
        print("\n")

if __name__ == "__main__":
    main()