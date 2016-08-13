Ensure that flask is installed.
sudo pip3 install flask

Next, install from the kad submodule
cd kad
python3 setup.py install


# flask-DHT

Use of example_dht (This must be running in order for lookup_dht to be used)
```
import example_dht as ed
dht = ed.get_dht()

#Spawn more nodes on different ports
ed.spread_dht()

#get peer info
peers = dht.peers()

#Push html into dht with the key 'html-body'
dht['html-body'] = "<h1> This was loaded from the DHT ;) </h1>"

#Start collecting BTC-e ticker data
ed.collect_btce()
```


Using lookup_dht spawns a new node on an open port
```
import lookup_dht as lu
dht = lu.get_dht()

#Returns list of all keys found in node
keys = lu.list_keys()

#Returns list of only peer id's 
peers = lu.get_peers()
```

To run the Flask application make sure that you have flask installed for python3
```
python3 DHT-web.py
```

To query for data collected by active nodes:
```https://127.0.0.1:5000/<key>```

example for btce ticker data:
```https://127.0.0.1:5000/btce-unixtimestamp```

To load homepage which includes the html that was stored using example_dht
```https://127.0.0.1/```
