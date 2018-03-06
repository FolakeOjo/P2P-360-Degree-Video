import peer, random

number_of_peers = random.randint(10,20)
peer_list = list()

for i in xrange(number_of_peers):
	peer_list.append(peer.peer())

for i in peer_list:
	print i.getTile()	