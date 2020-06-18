# day 19
import intcodecomputer
import copy
import os
import time

day19_input = [
109,424,203,1,21102,11,1,0,1105,1,282,21101,0,18,0,1105,1,259,2102,1,1,221,203,1,21102,1,31,0,1105,1,282,21102,1,38,0,1105,1,259,21002,23,1,2,21201,1,0,3,21101,0,1,1,21102,57,1,0,1105,1,303,2102,1,1,222,21002,221,1,3,21001,221,0,2,21102,1,259,1,21102,80,1,0,1105,1,225,21102,59,1,2,21102,1,91,0,1105,1,303,1202,1,1,223,21001,222,0,4,21102,259,1,3,21102,1,225,2,21101,225,0,1,21101,118,0,0,1105,1,225,21002,222,1,3,21102,1,112,2,21101,0,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,1201,1,0,223,20102,1,221,4,21002,222,1,3,21102,1,18,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,106,0,108,20207,1,223,2,21001,23,0,1,21102,1,-1,3,21102,1,214,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22101,0,-3,1,21202,-2,1,2,21201,-1,0,3,21101,250,0,0,1105,1,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,21202,-2,1,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21101,384,0,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2106,0,0
]

x=y=100

visited = {}
Left = False
while True:
	#print("checking {} {}".format(x,y),end="\r")
	if (x,y) in visited:
		output_1 = visited[(x,y)]
	else:
		drone1 = intcodecomputer.IntComputer("Drone", copy.copy(day19_input),[x,y],False)
		drone1.compute()
		visited[(x,y)] = drone1.lastoutput[0]
		output_1 = drone1.lastoutput[0]
	if output_1 == 0:
		y+=1
		x+=1
		if x == 800:
			x=left_edge
			y+=1
			print("{} {}".format(x,y))
			Left = False
		continue
	if Left == False: 
		if output_1 == 1:
			left_edge = x
			Left = True
	if (x+99,y) in visited:
		output_2 = visited[(x+99,y)]
	else:
		drone2 = intcodecomputer.IntComputer("Drone", copy.copy(day19_input),[x+99,y],False)
		drone2.compute()
		visited[(x+99,y)] = drone2.lastoutput[0]
		output_2 = drone2.lastoutput[0]
	if (x,y+99) in visited:
		output_3 = visited[(x,y+99)]
	else:
		drone3 = intcodecomputer.IntComputer("Drone", copy.copy(day19_input),[x,y+99],False)
		drone3.compute()
		visited[(x,y+99)] = drone3.lastoutput[0]
		output_3 = drone3.lastoutput[0]
	if (x+99,y+99) in visited:
		output_4 = visited[(x+99,y+99)]
	else:
		drone4 = intcodecomputer.IntComputer("Drone", copy.copy(day19_input),[x+99,y+99],False)
		drone4.compute()
		visited[(x+99,y+99)] = drone4.lastoutput[0]
		output_4 = drone4.lastoutput[0]
	if output_2 == 1 and output_3 == 1 and output_4 == 1:
		print ("found at {} {}".format(x,y))
		break
	x+=1
	if x == 800:
		x=0
		y+=1
		print("{} {}".format(x,y))
