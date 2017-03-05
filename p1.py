#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import socket
import orvibo
from orvibo.orvibo import Orvibo

import logging
logging.basicConfig()

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message_parts = [
                'VALORI DEL CLIENT:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'VALORI DEL SERVER:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',                '',
                'INTESTAZIONI RICEVUTE:',
                ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('%s=%s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        # global orv
        orv.emit_ir('aa.ir')
        # print orv.keep_connection 

        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8081), GetHandler)

    global orv
    orv = Orvibo('192.168.168.115','accf232991f4', 'irda')
    #orv.keep_connection = True
 
    print 'Server in esecuzione, usare <Ctrl-C> per interrompere'
    server.serve_forever()