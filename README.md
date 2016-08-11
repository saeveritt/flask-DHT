# flask-DHT

Use of example_dht (This must be running in order for lookup_dht to be used)
```
import example_dht as ed
dht = ed.get_dht()

#Spawn more nodes on different ports
ed.spread_dht()

#Push html into dht with the key 'html-body'
dht['html-body'] = "<h1> This was loaded from the DHT ;) </h1>"

#Start collecting BTC-e ticker data
ed.collect_btce()
```


Using lookup_dht
```
import lookup_dht as lu
dht = lu.get_dht()

#Returns list of all keys found in node
keys = lu.list_keys()

#Returns list of peers
peers = lu.get_peers()
```