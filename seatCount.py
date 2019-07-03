import math

seatSizeX = 120.00
seatSizeY = 70.00
hallway = 100.00
length = math.trunc( float( input( "What is the length = " ) ) ) * 100
width = round( float( input( "What is the width = " ) ) ) * 100
seatLess = 3
lengthResultX = length / seatSizeX
widthResultY = (width - hallway) / seatSizeY

print("You can fit {:.0f} number of seats in the classroom.".format(round( lengthResultX ) * round( widthResultY ) - seatLess))
