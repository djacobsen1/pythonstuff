import math as m

points = {"A": [1,2,4],
		  "B": [3,8,15],
		  "C": [3,4,7]}

def ReferencePoint(points):
	zero = [0,0,0]
	#Use Euclidean distance formula to calculate the distance between two points
	farthestdistance = 0
	for i in points:
		distance = m.sqrt(m.pow(abs(points[i][0]-zero[0]), 2) + m.pow(abs(points[i][1]-zero[1]), 2) + m.pow(abs(points[i][2]-zero[2]), 2))
		#Check against the current farthest point - if greater, reset the farthest point and assign the dictionary index
		if distance > farthestdistance:
			farthestdistance = distance
			farthestpoint = points[i]
	return farthestpoint
	
def FarthestNeighbor(points):
	startingpoint = ReferencePoint(points)
	farthestdistance = 0
	for i in points:
		if points[i] != startingpoint:
			distance = m.sqrt(m.pow(abs(points[i][0]-startingpoint[0]), 2) + m.pow(abs(points[i][1]-startingpoint[1]), 2) + m.pow(abs(points[i][2]-startingpoint[2]), 2))
			#Check the distance of the current point, if it further from the starting point than the current farthest distance,
			#then reset the farthest distance.
			if distance > farthestdistance:
				farthestdistance = distance
				farthestpoint = points[i]
	#return both the coordinates of the farthest point, and the distance from the point of reference.
	return (farthestpoint, farthestdistance)

def NearestNeighbor(points):
	startingpoint = ReferencePoint(points)
	farthestpoint, nearestdistance = FarthestNeighbor(points)
	for i in points:
		if points[i] != startingpoint:
			distance = m.sqrt(m.pow(abs(points[i][0]-startingpoint[0]), 2) + m.pow(abs(points[i][1]-startingpoint[1]), 2) + m.pow(abs(points[i][2]-startingpoint[2]), 2))
			if distance < nearestdistance:
				nearestdistance = distance
				nearestpoint = points[i]
				nearestpointname = i
	return (nearestpoint, nearestpointname)

print(NearestNeighbor(points))