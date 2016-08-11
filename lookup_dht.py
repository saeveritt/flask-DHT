from kad import *
from json import loads
from time import sleep
from hashlib import sha256

class CustomRequestHandler(kad.DHTRequestHandler):
	def handle_store(self,message):
		print(message['value'])
		return super(CustomRequestHandler,self).handle_store(message)

host1,port1 = 'localhost',1234
host2,port2 = 'localhost',0 #selects an open port

dht = kad.DHT(host2,port2,seeds=[(host1,port1)])

def search(key):
	return print(dht[key])

def list_keys(dht):
	keys = []
	for key in dht:
	    keys.append(key)
	return keys

def get_peers():
	peer_ids = []
	peers = dht.peers()
	count = len(peers)
	for i in  range(0,count):
		peer_ids.append(peers[i]['id'])
	return peer_ids

def get_id(pub_address):
	address = sha256(pub_address.encode()).hexdigest()
	nodeid = int(address,16)
	nodeid = int(str(nodeid)[0:38])
	return nodeid
def node(nodeid):
	return find_node(id=nodeid)

def identify():
	return dht.identity()

def rpc_ids():
	return dht.rpc_ids
def get_dht():
	return dht
