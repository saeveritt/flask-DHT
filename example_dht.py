import kad
from json import loads
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from time import sleep
import hashlib

host1,port1 = 'localhost',1234
dht1 = kad.DHT(host1,port1)

# Returns DHT object
def get_dht():
	return dht1

def gen_id(pub_address):
	h = hashlib.new('ripemd160',pub_address.encode())
	nodeid = h.hexdigest()
	return nodeid

# Add more nodes
def spread_dht():
	host2,port2 = 'localhost',1235
	host3,port3 = 'localhost',1236
	dht2 = kad.DHT(host2,port2,seeds=[(host1,port1)])
	dht3 = kad.DHT(host3,port3,seeds=[(host2,port2)])

#Continually collect btce data
def collect_btce():
	while True:
		try:
		    f = urlopen('https://btc-e.com/api/3/ticker/btc_usd-ppc_usd-ppc_btc-ltc_usd-ltc_btc-eth_usd-eth_btc-eth_ltc').read().decode()
		    f = loads(f)
		    key = 'btce-' + str(f['btc_usd']['updated'])
		    dht1[key] = f
		    print(key)
		    sleep(5)
		except (HTTPError, URLError):
	            pass

