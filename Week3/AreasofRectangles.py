'''
Solution based on topics covered in class 

The area of a rectangle is the rectangle’s length times its width.
Write a program that asks for the length and width of two rectangles.
The program should tell the user which rectangle has the greater area, or if the areas are the same
'''
#displaying what the program is about:

print('This program takes the length and width for two rectangles, calculates the area for each\
then compares the two areas')


#Using the approach of initializing variables
length1 = 0 #length of 1st rectangle
width1 = 0	#width of 1st rectangle
length2= 0  #length of 2nd rectangle
width2 = 0	#width of 2nd rectangle
area1 = 0	#area of 1st rectangle
area2 = 0 	#area of 2nd rectangle

#We can also declare all those variables in one line
length1,width1,length2,width2,area1,area2 = 0,0,0,0,0,0

#user input will be will be take for each 

#rectangle 1 dimensions
length1 = float(input('What\'s the length of 1st rectangle: '))
width1 = float(input('What\'s the width of 1st rectangle '))
area1 = length1*width1

#rectangle 2 dimensions
length2 = float(input('What\'s the length of 2nd rectangle '))
width2 =float(input('What\'s the width of 2st rectangle '))
area2 = length2*width2

#comparing two areas
#the output is formatted to produce a float with two decimals for the areas
if area1 > area2:
	print('The area of Rectangle 1 is:{:0.2f}\nThe area of Rectangle 2 is:{:0.2f}'.format(area1,area2))
	print('Rectangle 1 is bigger by: {:0.2f}'.format(area1-area2))

if area1 < area2:
	print('The area of Rectangle 1 is:{:0.2f}\nThe area of Rectangle 2 is:{:0.2f}'.format(area1,area2))
	print('Rectangle 2 is bigger by: {:0.2f}'.format(area2-area1))

if area1 == area2:
	print('The area of Rectangle 1 is:{:0.2f}\nThe area of Rectangle 2 is:{:0.2f}'.format(area1,area2))
	print('The two rectangles have the same area!! Coincedence? ')


















