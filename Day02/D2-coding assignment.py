#Print Personal Information
name = 'sk'
age = 19
city = 'Bng'
print(name)
print(age)
print(city)

#Two Numbers
a = 10
b = 16
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

#Find Square of a Number
a = 8
print(a**2)

#Find Cube of a Number
a = 7
print(a**3)

#Calculate Area of Rectangle Area = Length*Breadth
l = float(input(f'Enter the length of triangle: '))
b = float(input(f'Enter the Breadth of triangle: '))
a = l*b
print(f'Area of rectangle :{round(a,2)}')

#Calculate Perimeter of Rectangle P=2(l+b)
p = 2*(l+b)
print(f'perimeter of rectangle: {p}')

#Celsius to Fahrenheit Converter F=9/5*C+32
C = float(input(f'Enter the value of Celsius: '))
F = 9/5*C+32
print(f'Temperature: {F} fahrenheit')

#Calculate Simple Interest SI=100P×R×T/100
P = float(input(f'Enter the value of Principle amount: '))
R = float(input(f'Enter the value of Rate: '))
T = float(input(f'Enter the value of Time: '))
SI = P*T*R/100
print(f'simple intrest is {SI}')

#Percentage Calculator Percentage=obtained Marks/total Marks*100
OM = float(input(f'Enter the value of Obtained marks: '))
TM = 100
Percentage = OM/TM *100
print(f'your percentage is {Percentage}%')

#Swap Two Variables
a = 10
b = 16
a,b=b,a
print(a,b)

#Find Remainder
a = 10
b = 4
print(a%b)

#Find Power of a Number
print(2**4)

#Convert Minutes to Seconds : Seconds = Minutes * 60
minutes = int(input(f'Enter the number of minutes: '))
seconds = minutes*60
print(f'minutes: {minutes} seconds: {seconds}')

#Convert Kilometers to Meters
kilometers = float(input(f'Enter the number of kilometers: '))
meters = kilometers*1000
print(f'kilometers: {kilometers} meters: {meters}')

#Mini Bill Calculator
product = input(f'enter the product name: ')
quantity = int(input(f'Enter the quantity: '))
price_per_item = float(input(f'Enter the price: '))
total_bill = quantity*price_per_item
print(f'total bill: {total_bill}')
