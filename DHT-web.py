from flask import Flask
import lookup_dht as lu



app = Flask(__name__)

dht = lu.get_dht()

@app.route('/')
def home():
    body = dht['html-body']
    return body

@app.route('/keylist')
def keylist():
    return str(lu.list_keys(dht))

@app.route('/<key>')
def search(key):
    return str(dht[str(key)])

@app.route('/pair/<pair>')
def pair(pair):
	keylist = lu.list_keys(dht)
	data = []
	for key in keylist:
		pair = str(pair)
		last = dht[key][str(pair)]['last']
		high = dht[key][str(pair)]['high']
		low = dht[key][str(pair)]['low']
		volume = dht[key][str(pair)]['vol']
		updated = dht[key][str(pair)]['updated']
		data.append('{"pair": "%s" , "last": "%s" , "high": "%s" , "low": "%s" , "volume": "%s" , "updated": "%s"}'%(pair,last,high,low,volume,updated))
	return str(data)

if __name__ == "__main__":
    app.run()