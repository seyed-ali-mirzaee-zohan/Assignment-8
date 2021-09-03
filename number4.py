import pyfiglet
from termcolor import colored
result = pyfiglet.figlet_format("fraction", font = "digital" )
print(result)
print(colored(' Hello, Welcome to the fractions program ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' The following options are now available : ', 'white', attrs=['reverse', 'blink']))
print()
print(colored(' 1 : Addition       ', 'green', attrs=['reverse', 'blink']))
print(colored(' 2 : Multiplication ', 'yellow', attrs=['reverse', 'blink']))
print(colored(' 3 : Subtraction    ', 'green', attrs=['reverse', 'blink']))
print(colored(' 4 : Division       ', 'yellow', attrs=['reverse', 'blink']))
print()
enter=int(input( "Please enter your desired number : "))
print()

# تعریف کسر اول
print(colored(' first fraction ', 'green', attrs=['reverse', 'blink']))
numerator_1=int(input("Please enter the first fraction numerator : "))
denominator_1=int(input("Please enter the first fraction denominator : "))
fraction_1={'numerator': numerator_1 , 'denominator': denominator_1}

# تعریف کسر دوم
print(colored(' second fraction ', 'blue', attrs=['reverse', 'blink']))
numerator_2=int(input("Please enter the second fraction numerator : "))
denominator_2=int(input("Please enter the second fraction denominator : "))
fraction_2={'numerator': numerator_2 , 'denominator': denominator_2}

result={}

# تابع جمع
def Addition():
    result['numerator']=fraction_1['numerator']*fraction_2['denominator']+fraction_2['numerator']*fraction_1['denominator']
    result['denominator']=fraction_1['denominator']*fraction_2['denominator']
    return result

# تابع ضرب
def Multiplication():
    result['numerator']=fraction_1['numerator']*fraction_2['numerator']
    result['denominator']=fraction_1['denominator']*fraction_2['denominator']
    return result

# تابع تفریق
def subtraction():
    result['numerator']=fraction_1['numerator']*fraction_2['denominator']-fraction_2['numerator']*fraction_1['denominator']
    result['denominator']=fraction_1['denominator']*fraction_2['denominator']
    return result

# تابع تقسیم
def Division():
    result['numerator']=fraction_1['numerator']*fraction_2['denominator']
    result['denominator']=fraction_2['numerator']*fraction_1['denominator']
    return result


# فراخوانی توابع


# فراخوانی تابع جمع
if enter==1:
    A=Addition()
    print(A['numerator'],"/",A['denominator'])

# فراخوانی تابع ضرب
if enter==2:
    A=Multiplication()
    print(A['numerator'],"/",A['denominator'])

# فراخوانی تابع تفریق
if enter==3:
    A=subtraction()
    print(A['numerator'],"/",A['denominator'])

# فراخوانی تابع تقسیم
if enter==4:
    A=Division()
    print(A['numerator'],"/",A['denominator'])