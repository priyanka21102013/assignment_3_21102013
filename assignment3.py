# Q1 Binary Conversion
n = int(input("Enter the number"))
b = bin(n)
print(b)
print("\n")

# Q2 Calculator
n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
print("choose operator (+,-,*,/,%)")
operator = input("Enter operator")


if operator == "+":
   print(n1 + n2)
 elif operator == "-":
      print(n1 - n2)
 elif operator == "*":
      print(n1 * n2)
 elif operator == "%":
      print(n1 % n2)
 else:
     print("Invalid operation")

 print("\n")

# Q3 Math Library
A = (3=4)*5
print(A)

n = int(input("Enter the number"))
B = n*(n-1)/2

print(B)

import math
r = int(input("Enter the value"))
a = int(input("Enter the value"))
C = 4*math.pi*r**2
print(C)
D = math.sqrt(r*math.cos(a)**2+r*math.sin(a)**2)
print(D)

y2 = int(input("Enter the value"))
y1 = int(input("Enter the value"))
x2 = int(input("Enter the value"))
x1 = int(input("Enter the value"))
E = (y2-y1)/(x2-x1)
print(E)
print("\n")


#Q4 Range Expressions
print(list(range(5)))
print(list(range(3,10)))
print(list(range(4,13,3)))
print(list(range(15,5,-2)))
print(list(range(5,3)))
print("\n")

#Q5  Molecular weight
#Given, in grams/mole
H_Weight = 1.0079
C_Weight = 12.011
O_Weight = 15.9994

#Number of each element
H = int(input("Enter the number of H atom in the carbohydrate"))
C = int(input("Enter the number of C atoms in the carbohydrate"))
O = int(input("Enter the number of O atoms in the carbohydrate"))


# Calculations
Total_H_Weight = H*H_Weight
Total_C_weight = C*C_Weight
Total_O_ = O*O_Weight
Total_Weight = Total_H_Weight+Total_C_Weight+Total_O_Weight
print("The total weight of carbohydrate is", Total_Weight,"grams per mole")
print("\n")