
print("\n *_______________________* \n")
name =input("ENTER YOUR NAME :")
age =input("ENTER YOUR AGE :")
print("WELCOME ", name ,"YOUR AGE", age)
"""

print("\n *_______________________* \n")
x1 =input("ENTER THE FERST NAMBER :") 
y1 = input("ENTER THE SACAND NAMBER :") 
print("\n x + y =",int(x1)+int(y1) , "\n")


print("\n *_______________________* \n")
x1=65
y1=80
print("x= ", x1)
print("y= ", y1)
x1, y1= y1, x1
print("x= " , x1)
print("y= ", y1)


print("\n *_______________________* \n")
x2 =int(input ("ENTER THE FERST NAMBER : "))
y2 = int(input("ENTER THE SACAND NAMBER : ") )
z1 = input("ENTER THE Operatios :") 
if z1 == "+":
   print(x2 + y2)
elif z1 == "-":
   print(x2-y2)
elif z1 == "*":
   print(x2*y2)
elif z1 == "/" :
   print(x2/y2)
else :
   print("Try Again")



print("\n *_______________________* \n")
print("ENTER THREE NUMBERS")
a1 = int(input("ENTER NAMBER ONE : "))
a2 = int(input("ENTER NAMBER TWO : "))
a3 = int(input("ENTER NAMBER  THREE : "))
MAX = max(a1, a2, a3)
print("THE MAX NUMBER IS : ",MAX)

print("\n *_______________________* \n")
name =input("ENTER YOUR NAME :")
SUM1 =0
for i in range(1,6) :
   B = int(input("ENTER YOUR MARK 5 :"))
   if B > 100 :
     print("ENTER MARK <=100")
     B = int(input("ENTER YOUR MARK 5 :"))
     SUM1 =SUM1 + B

   else :
    SUM1 =SUM1 + B
print("THE SUM IS : ",SUM1)
AVG= float(SUM1/5) 
print("THE AVREG IS : ",AVG)  
if AVG >= 90 :
  print(" EXCELLENT")
else :
  if AVG >= 80  :
    print(" VERY GOOD") 
  elif AVG < 80 and AVG >=70 :
    print(" GOOD")
  elif AVG < 70 and AVG >=50 :
    print(" ACCEPTABLE")
  else :
    print(" FAILED") """