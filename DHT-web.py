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

if __name__ == "__main__":
    app.run()