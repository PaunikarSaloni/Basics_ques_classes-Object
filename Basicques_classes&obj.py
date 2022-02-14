# 1 Arithmetic Programming for addition , Subtraction , Multilication , Division
class Arithmetic:
    def add(self):
        a = 10
        b = 20
        print("Addition of a and b is :", a+b)
    
    def sub(self):
        a = 100
        b = 75
        print("Subtraction of a and b is :", a-b)
    
    def mul(self):
        a = 5
        b = 10
        print("Multiplication of a and b is :", a*b)

    def div(self):
        a = 50
        b = 5
        print("Division of a and b is :", a//b)

obj=Arithmetic()
obj.add()
obj.sub()
obj.mul()
obj.div()

#2 Program to calculate Area of Circle , Square , Rectangle , Triangle

class Area():
    def circle_area(self):
        r = 5
        print("Area of Circle is :", 3.14*r*r)

    def square_area(self):
        s = 4
        print("Area of Square is :",s*s)

    def rect_area(self):
        l = 5
        b = 8
        print("Area of Rectangle  is :",l*b)

    def triangle_area(self):
        l = 4
        b = 6
        print("Area of Triangle is :",0.5*l*b)

obj1 = Area()
obj1.circle_area()
obj1.square_area()
obj1.rect_area()
obj1.triangle_area()

#3 Program to calculate Volume of Cuboid , Cube , Cone , Cylinder

class Volume():
    def cuboid_volume(self):
        l = 5
        w = 7
        h = 9
        print("Volume of Cuboid is :", l*w*h)

    def cube_volume(self):
        a = 6
        print("Volume of Cube is :", a*a*a)

    def cone_volume(self):
        r = 5
        h = 7
        print("Volume of Cone is :",1/3*3.14*r*r*h)

    def cylinder_volume(self):
        r = 2
        h = 5
        print("Volume of Cylinder is :",3.14*r*h)

obj2 = Volume()
obj2.cuboid_volume()                                                           
obj2.cube_volume()
obj2.cone_volume()
obj2.cylinder_volume()

#4 Program to Swap two variables

class Swap:
    def swap_variables(self):
        x = 45
        y = 94
        z = x
        x = y
        y = z
        print("Swap Variables are :" , x,y)

obj3 = Swap()
obj3.swap_variables()

#5 Program to Reverse a three digit number

class Reverse():
    def reverse(self):
        num = 987
        rem1=num%10
        num=num//10
        rem2=num%10
        num=num//10
        rem3=num
        rev=rem1*100+rem2*10+rem3*1
        print("Reversed Number is:", rev)

obj4 = Reverse()
obj4.reverse()


#6 Program to convert kilometer to meter

class Km_to_m:
    def km(self):
        km = 5
        print("Meter : ", km*1000)

obj5 = Km_to_m()
obj5.km()


#7 Program to convert Celsius to Fahrenheit

class cel_fah:
    def temp(self):
        celsius = 40
        fahrenheit = (celsius * 1.8) + 32
        print("Temperature in Fahrenheit:", fahrenheit)

obj6 = cel_fah()
obj6.temp()

#8 Program to calculate (a+b)^2 and (a-b)^2

class Formula:
    def f1(self):
        a = 5
        b = 7
        f1 = (a*a +2*(a*b)+b*b)
        print("(a+b)^2 :" , f1)
    def f2(self):
        a = 6
        b = 10
        f2 = (a*a +2*(a*b)-b*b)
        print("(a-b)^2 :", f2)

obj7 = Formula()
obj7.f1()
obj7.f2()

