#Created by Matsuru Hoshi
#Created on March 6, 2019
#This file will print , "Hello, World!", to the CMD
import math

try:
    name = ""
    print("Welcome to the Circle Calculator 1000!")
    name = raw_input("What is your name? ")
    print( "Hello, " + str(name) + ". You opened the Circle Calculator 1000!")
    diameter = int(input("What is the diameter? "))

    circumference = 2 * (math.pi * (diameter/2))
    area = math.pi * (diameter/2) ** 2
    print( "The circumference is " + str(circumference))
    print( "The area is " + str(area))

    end = input( "Thank you!")
except NameError as err:
    print("Bad input: %s" % err)
except SyntaxError as err:
    print("Bad input")
