#!/usr/local/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from lib.orvibo.orvibo import Orvibo
import urllib.parse
import os.path
import logging
logging.basicConfig()

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)

        message = parsed_path.query + " OK "
      
        fname = parsed_path.query +".ir"

        if  os.path.isfile(fname) :
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(message, "utf8"))
            global orv
            orv.emit_ir(fname)
        else:
            message = fname + " not found "

            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(message, "utf8"))
         
        return

if __name__ == '__main__':
    server = HTTPServer(('', 8081), GetHandler)

    global orv
    orv = Orvibo('192.168.168.115','accf232991f4', 'irda')
    # orv.keep_connection = True
 
    print ('Server in esecuzione, usare <Ctrl-C> per interrompere')
    server.serve_forever()
