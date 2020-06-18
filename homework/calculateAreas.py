import sys
def calcSquareArea():
    side = float(input('Please enter the size of the square side: '))
    squareArea = side ** 2
    print(f'Square area is {squareArea} m^2')
    

def menuApp(userSelection):
    if userSelection == 1:
        calcSquareArea()
    elif userSelection == 2:
        print('rectangle')
    elif userSelection == 3:
        print('triangle')
    elif userSelection == 4:
        print('circle')
    elif userSelection == 5:
        print('Bye')
        sys.exit()
    else:
        return

def initApp():
    while True:
        print('Which figure would you like to calculate its area from?')
        print('\t1) Square\n\t2) Rectangle\n\t3) Triangle\n\t4) Circle\n\t5) None (Exit).\n')
        userSelection = int(input('Please choose an option: '))
        menuApp(userSelection)
        while True:
            userSelection = int(input('Non-valid option. Please choose a valid option: '))
            menuApp(userSelection)

initApp()
