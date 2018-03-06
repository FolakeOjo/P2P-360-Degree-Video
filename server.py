class server:

	def __init__(self,peer_list):
		self.peer_list = peer_list
		self.number_of_peers = len(peer_list)
		self.matchedpeers = list()

	def matchPeers()
		for i in xrange(self.number_of_peers):
			temp = list()
			temp.append(i)

			for j in xrange(self.number_of_peers):
				if i != j:
					r1 = peer_list[i].getResolution()
					c1 = peer_list[i].getCapacity()
					r2 = peer_list[j].getResolution()
					c2 = peer_list[j].getCapacity()
					if (r1 - r2 == 1 ) or (r1 - r2 == -1) or (r1 == r2):
						if (c1 - c2 < 0.5) and (c1 - c2 > -0.5):
							

