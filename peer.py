import random 
class peer:

	def  __init__(self):
		self.bandwidth = random.uniform(0.5,10) 
		self.resolution = random.randint(1,6)
		self.tile = list([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
		x = random.randint(1,2)
		y = random.randint(1,2)
		self.tile[x][y] = 2
		x_direction = random.randint(0,1)
		y_direction = random.randint(0,1)
		if x_direction == 0:
			x_direction = -1
		if y_direction == 0:
			y_direction = -1
		self.tile[x][y+y_direction] = random.randint(1,2)
		self.tile[x+x_direction][y] = random.randint(1,2)
		self.tile[x+x_direction][y+y_direction] = random.randint(1,2)

	def getTile(self):
		return self.tile

	def getBandwidth(self):
		return self.bandwidth

	def getResolution(self):
		return self.resolution