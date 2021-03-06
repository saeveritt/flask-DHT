from flask import Flask, render_template
import lookup_dht as lu
from subprocess import Popen, PIPE
from json import loads

app = Flask(__name__)

dht = lu.get_dht()

def rpc_command(command):
    f = Popen(['peerbox',str(command)],stdout=PIPE,stderr=PIPE)
    data,err = f.communicate()
    data = loads(data.decode('utf-8').replace('\n',''))
    return data

#type must match the includes label
def dht2file(key,type):
    data = dht[str(key)]
    f = open('templates/%s.html'%(type),'w')
    f.write(str(data))
    f.close()

@app.route('/')
def home():
    dht2file('html-body','body')
    dht2file('html-head','head')
    dht2file('html-table','table')
    data = rpc_command('-info')
    return render_template('body.html',ppc_version=data['ppc_version'],protocolversion=data['protocolversion'],walletversion=data['walletversion'],balance=data['balance'],newmint=data['newmint'],stake=data['stake'],blocks=data['blocks'],moneysupply=data['moneysupply'],connections=data['connections'],serial=data['serial'],ip=data['ip'],pos_difficulty=data['pos_difficulty'],pow_difficulty=data['pow_difficulty'],macc_addr=data['macc addr'],os=data['os'],hardware=data['hardware'],uptime=data['uptime'],average_load=data['average_load'])

@app.route('/keylist')
def keylist():
    return str(lu.list_keys(dht))

@app.route('/<key>')
def search(key):
    return str(dht[str(key)])

@app.route('/sendrawtransaction/<rawtx>')
def pushtx(rawtx):
    f = Popen(['ppcoind','sendrawtransaction',str(rawtx)],stdout=PIPE,stderr=PIPE)
    rawtx,err = f.communicate()
    rawtx = rawtx.decode('utf-8').replace('\n','')
    err = err.decode('utf-8').replace('\n','')
    return '{"txid": "%s" ,"%s"}'%(rawtx,err)

@app.route('/getinfo')
def getinfo():
    f = Popen(['ppcoind','getinfo'],stdout=PIPE,stderr=PIPE)
    data,err = f.communicate()
    data = loads(data.decode('utf-8').replace('\n',''))
    version = data['version']
    protocolversion = data['protocolversion']
    walletversion = data['walletversion']
    balance = data['balance']
    newmint = data['newmint']
    stake = data['stake']
    blocks = data['blocks']
    moneysupply = data['moneysupply']
    connections = data['connections']
    proxy = data['proxy']
    ip = data['ip']
    difficulty = data['difficulty']
    testnet = data['testnet']
    keypoololdest = data['keypoololdest']
    keypoolsize = data['keypoolsize']
    paytxfee = data['paytxfee']
    errors = data['errors']
    return render_template('basic.html',version = version, protocolversion = protocolversion, walletversion = walletversion, balance = balance, newmint = newmint, stake = stake,blocks = blocks , moneysupply = moneysupply , connections = connections, proxy = proxy,ip = ip , difficutly = difficulty , testnet = testnet , keypoololdest = keypoololdest,keypoolsize = keypoolsize , paytxfee = paytxfee , errors = errors)

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
