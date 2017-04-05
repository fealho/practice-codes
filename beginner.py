from sys import stdin

#Prints the number of necessary leds to implement a number,
#where each number needs a certain amount of leds according to the list:
#[6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

#param: x string with the number to be converted
#return: num of LEDs to implement the number
def numLEDs(x):
	LEDperDigit = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
	return sum( [ LEDperDigit[ int(digit) ] for digit in x ] )

assert numLEDs("0") == 6
assert numLEDs("19") == 8
assert numLEDs("115380") == 27

#reads the file
lines = input()
intList = [raw_input() for line in range(lines)]
numLEDs = [numLEDs( str(num) ) for num in intList]

for numLED in numLEDs:
	print numLED, "leds"


'''
STEPS TO SUBMIT TO GIT:

1) git init .
2) git status
3) git add -A
4) git commit -m "Initial commit."
5) CREATE ON GITHUB
6) git remote add origin https://github.com/fealho/practice-codes.git
7) git push -u origin master
'''

#TO DO: add URL
#change to python 3
#use underscore for var
#dont convert to str, use mod 10
#make tuple of list LED, since thats immutable
#LEDperDigit should be global, since I'm recreating it 