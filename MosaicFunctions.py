# Version 0.3 Veranstaltung: Objektorientierte Programmierung
# Author: Prof. Dr. Margarita Esponda

"""	In this homework you have to program the inside of six diferent 'decide_color_..' functions.
        The functions calculate and returns a color for each (x,y) position of a square of side = size.
        
        The functions are used in the modul'MosaicFrames.py' which shows the diferent pictures (mosaics)
        on a window.
        
        We wrote some simple examples of decide_color functions
        Please overwrite them with your own solutions.

        The 'MosaicFrames.py' file and this file have to be in the same directory and you must start the programm
        with 'MosaicFrames.py'.
"""

def decide_color_squares(x, y, size):
	if (x > size // 4) and (x <= size // 2) and (y > size // 4) and (y <= size // 2):
		return 'RED'
	if (x >= size // 2) and (x < (size // 4)*3) and (y >= size // 2) and (y < (size // 4)*3):
		return 'RED'
	else:
		return 'BLACK'

def decide_color_diags(x, y, size):
    # overwrite the content of the function
	achtel=size//8
	if (x==y) or (abs(x-y)==achtel) or (abs(x-y)==(2*achtel)) or (abs(x-y)==(3*achtel)): 
		return 'RED'
	if (abs(x-y)==(4*achtel)) or (abs(x-y)==(5*achtel)) or (abs(x-y)==(6*achtel)) or (abs(x-y)==(7*achtel)):
		return 'RED'
    	else:
        	return 'YELLOW'

def decide_color_triangles(x, y, size):
	sixth=size//6
	if (x <= size // 2):
		if (y > 4*sixth) and (y <= 5*sixth) and (x > sixth) and (x <= 2*sixth):
			if ((x+y)<=size):				
				return 'ORANGE'
			else:
				return 'GREEN'
		return 'BLUE'
	else:
		if ((x+y)<=size):
			return 'GREY'
		if ((x-y)<0):
			return 'GREEN'
	return 'WHITE'


def decide_color_circle(x, y, size):
	radius = size // 4
	mitte = size // 2
	cquadrat = ((x-mitte)**2)+((y-mitte)**2) 
	if (cquadrat <= (radius**2)):
		if (x <= mitte ):
			return 'WHITE'
		else:
			return 'RED'
	if (y <= mitte ):
		return 'BLUE'
	else:
		return 'GRAY'


def decide_color_chess(x, y, size):
	achtel = size // 8
	if (x <= achtel) or ((x > 2*achtel)and(x <= 3*achtel)) or ((x > 4*achtel)and(x <= 5*achtel)) or ((x > 6*achtel)and(x <= 7*achtel)):
		if (y <= achtel) or ((y > 2*achtel)and(y <= 3*achtel)) or ((y > 4*achtel)and(y <= 5*achtel)) or ((y > 6*achtel)and(y <= 7*achtel)):
			return 'BLACK'
		else:
			return 'WHITE'
	else:
		if (y <= achtel) or ((y > 2*achtel)and(y <= 3*achtel)) or ((y > 4*achtel)and(y <= 5*achtel)) or ((y > 6*achtel)and(y <= 7*achtel)):
			return 'WHITE'
		else:
			return 'BLACK'
    	return 'BLACK'

def decide_color_illusion_1(x, y, size):
    # overwrite the content of the function
    return "WHITE"

def decide_color_illusion_2(x, y, size):
    # overwrite the content of the function
    return "black"

def decide_color_illusion_3(x, y, size):
    # overwrite the content of the function
    return 'WHITE'

def decide_color_own_picture(x, y, size):
    return 'GRAY'
