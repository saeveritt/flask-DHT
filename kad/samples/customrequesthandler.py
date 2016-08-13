from kad import *

class CustomRequestHandler (kad.DHTRequestHandler):
    def handle_store(self, message):
        print (message['value'])
        return super (CustomRequestHandler, self).handle_store (message)

    
d = DHT ('localhost', 3030, requesthandler=CustomRequestHandler)
    
d['ciao'] = {'hola': 12}
