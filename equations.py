import math

def main():
    #Variables
    n = 0
    a,b,c = 0,0,0

    #Sum to N natural numbers
    n_nat = (n*(n-1))/2

    #Quadratic Equation
    q_e1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    q_e2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)

    #Trig Identities
    c_2 = (math.cos(a-b)+math.cos(a+b))/2 #cos(a)*cos(b)
    s_c = (math.sin(a-b)+math.sin(a+b))/2 #sin(a)*cos(b)

if __name__ == "__main__":
    main()