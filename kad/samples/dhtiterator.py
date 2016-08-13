from kad import DHT

d = DHT ('localhost', 3100)

d['ciao'] = 'mondo'
d['hello'] = 'world'

for key in d:
    print (key, d[key])
