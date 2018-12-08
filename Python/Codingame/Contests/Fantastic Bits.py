import sys
import math

myTeamId = int(input())

if myTeamId == 1:

	opponentGoalCenterX = 0
	opponentGoalCenterY = 3750


else:

	opponentGoalCenterX = 16000
	opponentGoalCenterY = 3750


def distance(x1, y1, x2, y2):

	return math.sqrt(math.pow(x1-x2,2)+math.pow(x1-x2,2))

while True:

	
	Snaffles = []
	Wizards = []
	

	myScore, myMagic = [int(i) for i in raw_input().split()]
	myScore += 1
	opponentScore, opponentMagic = [int(i) for i in raw_input().split()]
	entities = int(raw_input())
	

	for i in xrange(entities):
		
		id, Type, x, y, vx, vy, state = raw_input().split()
		id = int(id)
		x = int(x)
		y = int(y)
		vx = int(vx)
		vy = int(vy)
		state = int(state)
		
		
		if Type == "WIZARD":
			Wizards.append([x, y, state])
	
		elif Type == "SNAFFLE":
			Snaffles.append([id, x, y, state])


	for Wizard in Wizards:
		
		if Wizard[2] == 1:
		
			print "THROW", opponentGoalCenterX, opponentGoalCenterY, 500


		else:

			closestSnaffle = None
			closestSnaffleDistance = 100000
			
			for Snaffle in Snaffles:

				if distance(Wizard[0], Wizard[1], Snaffle[1], Snaffle[2]) < closestSnaffleDistance:
					if Wizard == 1:

						if Snaffle[3] == 0:
							closestSnaffleDistance1 = distance(Wizard[0], Wizard[1], Snaffle[1], Snaffle[2])
					if Snaffle[3] == 0:
						
						closestSnaffleDistance = distance(Wizard[0], Wizard[1], Snaffle[1], Snaffle[2])
						closestSnaffle = Snaffle

					else:
						continue
			

			if (distance(Wizard[0], Wizard[1], Snaffle[1], Snaffle[2]) < 2000) and myMagic >= 20:
				print "FLIPENDO", closestSnaffle[0]

			else:
				print "MOVE", closestSnaffle[1], closestSnaffle[2], 150