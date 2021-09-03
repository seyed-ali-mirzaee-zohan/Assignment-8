from pyfiglet import Figlet
from termcolor import colored
f=Figlet(font='banner3-D')
print(colored((f.renderText('star')),'yellow'))
print(colored(' Hello, Welcome to the program ', 'blue', attrs=['reverse', 'blink']))
print()
enter=int(input('Please enter your desired number : '))
print()
def show():
    for i in range(1,enter+1):
        print(' '*(enter-i),"*"*(2*i-1))
    counter=enter-1
    for i in range(enter+1):
        print(' '*(enter-counter),"*"*(2*counter-1))
        counter-=1
show()