'''
Solution - Based on topics covered in class so far

Problem

Assuming the ocean’s level is currently rising at about 1.6 millimeters per year,
create an application that displays the number of millimeters that the ocean will have risen each year
for the next 25 years.

'''
#What the program does
 

riseLevel = 1.6 #increase every year of 1.6 mm
number_of_years = 1 #initialize number of years 
increase_level = 0 #initialize the total rise 

while number_of_years<=25:
	increase_level+=riseLevel
	print('Ocean level increase after {:d} year(s) is: {:.1f}mm'.format(number_of_years,increase_level))
	number_of_years+=1 #increment to next year


print('After 25 years, the ocean level has increased by {:.1f} mm'.format(increase_level))