import pyfiglet
from termcolor import colored
result = pyfiglet.figlet_format("Complex numbers", font = "digital" )
print(result)
print(colored(' Hello, Welcome to the program ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' The following options are now available : ', 'white', attrs=['reverse', 'blink']))
print()
print(colored(' 1 : Addition       ', 'green', attrs=['reverse', 'blink']))
print(colored(' 2 : Multiplication ', 'yellow', attrs=['reverse', 'blink']))
print(colored(' 3 : Subtraction    ', 'green', attrs=['reverse', 'blink']))
print()
enter=int(input( "Please enter your desired number : "))
print()
print(colored(' General format = ', 'green', attrs=['reverse', 'blink']),colored(' A+Bi ', 'yellow', attrs=['reverse', 'blink']))
print()

# تعریف عدد مختلط اول
print(colored(' first Complex number ', 'blue', attrs=['reverse', 'blink'])) 
a=int(input("please enter the amount of a : "))
b=int(input("please enter the amount of b : "))

# تعریف عدد مختلط دوم
print(colored(' second Complex number ', 'blue', attrs=['reverse', 'blink']))
c=int(input("please enter the amount of c : "))
d=int(input("please enter the amount of d : "))

# تابع جمع
def addition():
    A=(a+c)
    B=(b+d)
    print(A,"+",B,'*i')

# تابع ضرب
def multiplication():
    A=(a*c-b*d)
    B=(a*d+b*c)
    print(A,"+",B,'*i')

# تابع تفریق
def subtraction():
    A=(a-c)
    B=(b-d)
    print(A,"+",B,'*i')


# فراخوانی توابع


# فراخوانی تابع جمع
if enter==1:
    addition()

# فراخوانی تابع ضرب
if enter==2:
    multiplication()

# فراخوانی تابع تفریق
if enter==3:
    subtraction()