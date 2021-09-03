import pyfiglet
from termcolor import colored
result = pyfiglet.figlet_format("Time", font = "digital" )
print(result)
print(colored(' Hello, Welcome to the program ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' The following options are now available : ', 'white', attrs=['reverse', 'blink']))
print()
print(colored(' 1 : Addition       ', 'green', attrs=['reverse', 'blink']))
print(colored(' 2 : Subtraction    ', 'yellow', attrs=['reverse', 'blink']))
print(colored(' 3 : Second ⇨ Time  ', 'green', attrs=['reverse', 'blink']))
print(colored(' 4 : Time ⇨ Second  ', 'yellow', attrs=['reverse', 'blink']))
print()
enter=int(input("Please enter your desired number : "))
print()

result={}

# تابع جمع
def Addition():
    # تعریف زمان اول
    print(colored(' first Time ', 'green', attrs=['reverse', 'blink']))
    time1=input("Please enter the first time (h:m:s) :  ")
    time_1=time1.split(":")
    time_1={"h":int(time_1[0]),"m":int(time_1[1]),"s":int(time_1[2])}

    # تعریف زمان دوم
    print(colored(' second Time ', 'blue', attrs=['reverse', 'blink']))
    time2=input("Please enter the second time (h:m:s) : ")
    time_2=time2.split(":")
    time_2={"h":int(time_2[0]),"m":int(time_2[1]),"s":int(time_2[2])}

    result["h"]=time_1["h"]+time_2["h"]
    result["m"]=time_1["m"]+time_2["m"]
    result["s"]=time_1["s"]+time_2["s"]
    if result["s"]>=60:
       result["s"]-=60
       result["m"]+=1 
    if result["m"]>=60:
       result["m"]-=60
       result["h"]+=1 
    return result

# تابع تفریق
def subtraction():
    # تعریف زمان اول
    print(colored(' first Time ', 'green', attrs=['reverse', 'blink']))
    time1=input("Please enter the first time (h:m:s) :  ")
    time_1=time1.split(":")
    time_1={"h":int(time_1[0]),"m":int(time_1[1]),"s":int(time_1[2])}

    # تعریف زمان دوم
    print(colored(' second Time ', 'blue', attrs=['reverse', 'blink']))
    time2=input("Please enter the second time (h:m:s) : ")
    time_2=time2.split(":")
    time_2={"h":int(time_2[0]),"m":int(time_2[1]),"s":int(time_2[2])}

    Total_seconds_1=time_1["h"]*3600+time_1["m"]*60+time_1["s"]
    Total_seconds_2=time_2["h"]*3600+time_2["m"]*60+time_2["s"]

    if Total_seconds_1>=Total_seconds_2:
        seconds=Total_seconds_1-Total_seconds_2
        hour=seconds//3600
        total_Minutes=seconds-3600*hour
        minutes=total_Minutes//60
        second=total_Minutes-60*minutes
        print(hour,':',minutes,':',second)
    else:
        seconds=Total_seconds_2-Total_seconds_1
        hour=seconds//3600
        total_Minutes=seconds-3600*hour
        minutes=total_Minutes//60
        second=total_Minutes-60*minutes
        print(hour,':',minutes,':',second)

# تابع تبدیل ثانیه به زمان
def second_to_time():
    Seconds=int(input( "Please enter the seconds : "))
    Hour=Seconds//3600
    total_Minutes=Seconds-3600*Hour
    Minutes=total_Minutes//60
    Second=total_Minutes-60*Minutes
    print(Hour,":",Minutes,":",Second)

# تابع تبدیل زمان به ثانیه
def time_to_second():
    time1=input("Please enter your time (h:m:s) :  ")
    time_1=time1.split(":")
    time_1={"h":int(time_1[0]),"m":int(time_1[1]),"s":int(time_1[2])}
    seconds=time_1["h"]*3600+time_1["m"]*60+time_1["s"]
    print("seconds : ",seconds)


# فراخوانی توابع


# فراخوانی تابع جمع
if enter==1:
    A=Addition()
    print(A["h"],':',A["m"],':',A["s"])

# فراخوانی تابع تفریق
if enter==2:
    subtraction()

# فراخوانی تابع تبدیل ثانیه به زمان
if enter==3:
    second_to_time()

# فراخوانی تابع تبدیل زمان به ثانیه
if enter==4:
    time_to_second()